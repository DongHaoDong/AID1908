import requests
import time
import random
from hashlib import md5


class YdSpider(object):
    def __init__(self):
        # F12抓到的Request URL中的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # 检查频率最高的三个字段:Cookie Referer User-Agent
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "238",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=112756945@10.169.0.83; JSESSIONID=aaa5piNGBICPKfRvmZw8w; OUTFOX_SEARCH_USER_ID_NCOO=272803976.2557563; ___rl__test__cookies=1576637855122",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    # ts salt sign
    def get_ts_salt_sign(self,word):
        # ts
        ts = str(int(time.time())*1000)
        # salt
        salt = ts + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return ts,salt,sign

    # 攻克有道
    def attack_yd(self,word):
        ts,salt,sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "316dd52438d41a1d675c1d848edf4877",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        res = requests.post(
            url=self.post_url,
            data=data,
            headers=self.headers
        )
        # res.json()直接得到python数据类型-字典
        html = res.json()
        result = html["translateResult"][0][0]['tgt']
        return result

    def run(self):
        word = input("请输入要翻译的单词:")
        result = self.attack_yd(word)
        print('翻译结果:',result)

if __name__ == '__main__':
    sipder = YdSpider()
    sipder.run()



