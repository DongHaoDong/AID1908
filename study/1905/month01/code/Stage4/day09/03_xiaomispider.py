import json

import requests
from threading import Thread
from queue import Queue
import time
import csv
from threading import Lock
from fake_useragent import UserAgent
from lxml import etree

class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        # 创建空队列
        self.q = Queue()
        # 打开文件,保存csv
        self.f = open('xiaomi.csv','a',encoding='utf8')
        self.writer = csv.writer(self.f)
        # 创建线程锁，用于多个线程写入同一个文件
        self.lock = Lock()

    # 随机获取请求头
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    # 类型+类型码
    def get_code(self):
        one_url = "http://app.mi.com/category/13"
        html = requests.get(
            url=one_url,
            headers=self.get_headers()
        ).text
        # 解析
        parse_obj = etree.HTML(html)
        li_list = parse_obj.xpath('//ul[@class="category-list"]/li')
        for li in li_list:
            app_type = li.xpath('./a/text()')[0]
            app_code = li.xpath('./a/@href')[0].split('/')[-1]
            app_total = self.get_app_total(app_code)
            # 把每个类别的所有页的URL地址入列
            self.url_in(app_total,app_code)

    # 获取某个类别的总页数
    def get_app_total(self,app_code):
        url = self.url.format(1,app_code)
        html = requests.get(
            url=url,
            headers=self.get_headers()
        ).text
        html = json.loads(html)
        app_total = html['count'] // 30 + 1
        return app_total


    # url入队列
    def url_in(self,app_total,app_code):
        for page in range(0,app_total):
            url = self.url.format(page,app_code)
            self.q.put(url)

    # 线程事件函数 - 请求 + 解析 + 保存
    def parse_page(self):
        while True:
            # 每抓取一页将数据写入到csv文件
            app_list = []
            # 队列不为空时，再get()
            if not self.q.empty():
                url = self.q.get()
                html = requests.get(url=url, headers=self.get_headers()).json()
                for app in html['data']:
                    name = app['displayName']
                    link = 'http://app.mi.com/details?id='+app['packageName']
                    print(name,link)
                    app_list.append((name,link))
                # 加锁
                self.lock.acquire()
                self.writer.writerows(app_list)
                # 释放锁
                self.lock.release()
            else:
                break

    # 入口函数
    def run(self):
        # url入队列
        self.get_code()
        # 创建 多线程
        t_list = []
        for i in range(10):
            t = Thread(target=self.parse_page)
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()
        # 抓取完成后关闭文件
        self.f.close()


if __name__ == '__main__':
    begin = time.time()
    spider = XiaomiSpider()
    spider.run()
    end = time.time()
    print("执行时间:%2.f"%(end-begin))