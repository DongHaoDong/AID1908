import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # 抓取的url地址
        self.url = 'http://www.renren.com/973116780/profile'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }

    def get_cookies(self):
        cookies = {}
        cookies_str = 'anonymid=k4c0r1yz-pzvxkf; depovince=GW; _r01_=1; JSESSIONID=abcDAiw02y0mU64ddRB8w; ick_login=83f80a9a-2b55-40f3-8685-88a6144f0626; t=f41b47d87ea76c271cb60f84bd6706660; societyguester=f41b47d87ea76c271cb60f84bd6706660; id=973116780; xnsid=e4530f4b; ver=7.0; loginfrom=null; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341787; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341792; wp_fold=0; jebecookies=cd8b6928-eee7-4bde-a161-7933a4f284d8|||||; XNESSESSIONID=ead277ab8d81'
        for kv in cookies_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value
        return cookies

    def get_parse_html(self):
        cookies = self.get_cookies()
        html = requests.get(
            url=self.url,
            headers=self.headers,
            # cookies参数,类型为字典
            cookies=cookies,
        ).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        # r_list['就读于国家检察官学院']
        print(r_list)

    def run(self):
        self.get_parse_html()


if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()