import requests
from lxml import etree
from fake_useragent import UserAgent
import os


class CodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1907/13-Redis/'
        self.auth = ('tarenacode','code_2013')

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    def parse_html(self):
        # 1. 获取响应
        html = requests.get(
            url=self.url,
            auth=self.auth,
            headers=self.get_headers()
        ).text
        # 2. 解析响应内容
        parse_obj = etree.HTML(html)
        href_list = parse_obj.xpath('//a/@href')
        # 只提取.zip|.rar|.tar.gz的文件
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar') or href.endswith('.tar.gz'):
                self.save_file(href)

    def save_file(self,href):
        base_directory = 'D:/'
        directory = base_directory + '/'.join(self.url.split('/')[3:-1]) + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 下载链接
        file_url = self.url + href
        html = requests.get(
            url=file_url,
            auth=self.auth,
            headers=self.get_headers()
        ).content
        filename = directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print(href,'下载成功')

    def run(self):
        self.parse_html()


if __name__ == "__main__":
    spider = CodeSpider()
    spider.run()