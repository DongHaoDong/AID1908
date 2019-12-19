import requests
import json
import re
import execjs


class BaiduTranslateSpider(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            "cookie": "BIDUPSID=10654A2CFBEA2F15A893A2E2FF68A8A9; PSTM=1576175989; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BAIDUID=10654A2CFBEA2F150E0109A25E628154:SL=0:NR=10:FG=1; delPer=0; PSINO=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; sideAdClose=18249; H_PS_PSSID=1454_21116_30211_30283; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1576642503,1576764598,1576765700,1576767418; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1576767418; __yjsv5_shitong=1.0_7_95958817e0e9f0f806df35f4c7b00392d131_300_1576767421965_124.89.86.156_41c36524; yjs_js_security_passport=e67cadd372d2371c6436e1cc08c2961b9998eb55_1576767432_js",
            "referer": "https://fanyi.baidu.com/?aldtype=16047",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }

    # 获取token+gtk
    def get_token_gtk(self):
        html = requests.get(
            url=self.get_url,
            headers=self.headers
        ).text
        gtk_re = "window.gtk = '(.*?)'"
        token_re = "token: '(.*?)'"
        # 获取gtk
        pattern = re.compile(gtk_re)
        gtk = pattern.findall(html)[0]
        # 获取token
        pattern = re.compile(token_re)
        token = pattern.findall(html)[0]
        return token,gtk

    # 获取sign
    def get_sign(self,word,gtk):
        with open('translate.js','r') as f:
            js_data = f.read()
        exec_obj = execjs.compile(js_data)
        sign = exec_obj.eval('e("'+word+'","'+gtk+'")')
        return sign

    # 入口函数
    def run(self):
        word = input("请输入要翻译的单词:")
        token,gtk = self.get_token_gtk()
        sign = self.get_sign(word,gtk)
        data = {
            "from": "zh",
            "to": "en",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
        }
        html = requests.post(
            url=self.post_url,
            data=data,
            headers=self.headers
        ).json()
        result = html['trans_result']['data'][0]['dst']
        print(result)


if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    spider.run()
