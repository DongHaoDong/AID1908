import requests
url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
# 定义代理，在代理IP网站中查找免费代理IP
proxies = {
    'http':'http://183.167.217.152:63000',
    'https':'https://183.167.217.152:63000'
}
html = requests.get(url,proxies=proxies,headers=headers,timeout=10).text
print(html)