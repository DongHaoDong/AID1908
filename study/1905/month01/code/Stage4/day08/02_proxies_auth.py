'''私密代理+独享代理'''
import requests
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = {
    'http':'http://309435365:szayclhp@222.95.144.38:3000',
    'https':'https://309435365:szayclhp@222.95.144.38:3000',
}
html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)


