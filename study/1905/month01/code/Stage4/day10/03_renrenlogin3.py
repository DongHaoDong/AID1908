import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # post_url为form表单中action对应的URL地址
        self.post_url = 'http://www.renren.com/PLogin.do'
        # 真正要抓取的页面的url地址 - 个人主页
        self.get_url = 'http://www.renren.com/970294164/profile'
        # 实例化session = requests.session()
        self.session = requests.session()
    # 提取数据 - 先post再get
    def parse_html(self):
        data = {
            'email':'15110225726',
            'password':'zhanshen001'
        }
        # 1. 先post,把cookie保存在session对象中 - 会话保持
        self.session.post(url=self.post_url,data=data)
        # 再get,正常抓取数据
        html = self.session.get(url=self.get_url).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        print(r_list)

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()
