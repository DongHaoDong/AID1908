# 导入selenium的webserver接口
from selenium import webdriver
from selenium.webdriver import ActionChains
import pymysql

class GovSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.binary_location = r"D:\Chrome\Application\chrome.exe"
        self.browser = webdriver.Chrome(options=self.options)
        self.db = pymysql.connect(
            '127.0.0.1',
            'root',
            '584023982',
            'govdb'
        )
        self.cursor = self.db.cursor()
        # 创建三个大列表,为executemany()使用
        self.province = []
        self.city = []
        self.country = []

    def get_data(self):
        self.browser.get(self.url)
        xpath_bds = '//td[@class="arlisttd"]/a[contains(@title,"行政区划代码")]'
        # 一定要用element,找最新节点
        a = self.browser.find_element_by_xpath(xpath_bds)
        # get_attribute()方法可提取属性值,连接会自动补全域名
        href = a.get_attribute('href')
        # 和version表中查询,得到一个结果result
        sel = "select * from version where url=%s"
        # result返回受影响条数
        result = self.cursor.execute(sel,[href])
        if result:
            print("网站未更新,无需抓取")
        else:
            a.click()
            self.get_code()
            # 把href插入到version表中,表中只保留最新的一条连接
            delete = 'delete from version'
            ins = 'insert into version values(%s)'
            self.cursor.execute(delete)
            self.cursor.execute(ins,[href])
            self.db.commit()

    # 真正抓取数据的函数
    def get_code(self):
        # 1. 切换句柄
        all_headers = self.browser.window_handles
        self.browser.switch_to.window(all_headers[1])
        # 2. 抓数据
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name,code)
            if code[-4:] == '0000':
                self.province.append([name,code])
                # 把直辖市加到省表
                if name in ['北京市','天津市','上海市','重庆市']:
                    self.city.append([name,code,code])
            elif code[-2:] == '00':
                self.city.append([name,code,(code[:2]+'0000')])
            else:
                if code[:2] in ['11','12','31','50']:
                    self.country.append([name,code,(code[:2]+'0000')])
                else:
                    self.country.append([name,code,(code[:4]+'00')])

        # 把所有数据存入数据库
        self.insert_mysql()

    def insert_mysql(self):
        # 先清空表
        del1 = 'delete from province'
        del2 = 'delete from city'
        del3 = 'delete from country'
        self.cursor.execute(del1)
        self.cursor.execute(del2)
        self.cursor.execute(del3)
        self.db.commit()
        # 再插入表
        ins1 = 'insert into province values(%s,%s)'
        ins2 = 'insert into city values(%s,%s,%s)'
        ins3 = 'insert into country values(%s,%s,%s)'
        self.cursor.executemany(ins1,self.province)
        self.cursor.executemany(ins2,self.city)
        self.cursor.executemany(ins3,self.country)
        self.db.commit()
    def run(self):
        self.get_data()


if __name__ == '__main__':
    spider = GovSpider()
    spider.run()


