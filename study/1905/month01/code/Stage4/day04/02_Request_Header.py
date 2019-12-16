'''
http://httpbin.org/get发请求，查看自己请求头
'''
import urllib.request
# res为对象
url = 'http://httpbin.org/get'
res = urllib.request.urlopen(url)
# 1. html为字符串(特别长)
# read():bytes read().decode():string
html = res.read().decode('utf-8')
print(html)