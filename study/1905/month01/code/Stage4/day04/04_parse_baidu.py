from urllib import request
from urllib import parse
import time

# 1. 拼接url地址函数
def get_url(word):
    baseurl = 'http://www.baidu.com/s?'
    #编码+拼接
    params = parse.urlencode({'wd':word})
    url = baseurl + params
    return url
# 2. 请求+保存
def write_html(url,word):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    # 拿到响应内容
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 保存到本地文件
    filename = word + '.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

# 主程序入口
if __name__ == '__main__':
    word = input('请输入要搜索的内容:')
    url = get_url(word)
    while True:
        try:
            write_html(url, word)
            break
        except Exception as e:
            time.sleep(0.5)

