import requests
from lxml import etree
import re


class GovSpider(object):
    def __init__(self):
        self.url = "http://www.mca.gov.cn/article/sj/xzqh/2019/"
        self.headers = {'User-Agent':'Mozilla/5.0'}

    # 提取最新的行政区划代码链接
    def get_false_url(self):
        html = requests.get(self.url,headers=self.headers).text
        parse_html = etree.HTML(html)
        # 把14个a节点对象提取出来
        # for循环依次遍历，寻找最新链接
        # 判断名字是否以行政区划代码结尾,如果是,则仕最新的,break
        # a_list:a节点对象列表
        a_list = parse_html.xpath('//a[@class="artitlelist"]')
        for a in a_list:
            # name: '2019年10月xxx变更情况',从当前节点获取属性值，get('属性名')
            name = a.get('title')
            if name.endswith('行政区划代码'):
                false_url = "http://www.mca.gov.cn" + a.get('href')
                # 利用假链接,获取真实链接
                self.get_real_url(false_url)
                break

    # 获取响应内容,分析js，提取真实url
    def get_real_url(self,false_url):
        html = requests.get(
            url=false_url,
            headers=self.headers
        ).text
        # 正则提取新链接
        re_bds = 'window.location.href="(.*?)"'
        pattern = re.compile(re_bds,re.S)
        real_url = pattern.findall(html)[0].strip()
        # 提取数据
        self.get_data(real_url)

    def get_data(self,real_url):
        # 发请求得到html+xpath提取北京市11000
        html = requests.get(
            url=real_url,
            headers=self.headers
        ).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.xpath('./td[2]/text()')[0].strip()
            name = tr.xpath('./td[3]/text()')[0].strip()
            print(name,code)










if __name__ == '__main__':
    spider = GovSpider()
    spider.get_false_url()