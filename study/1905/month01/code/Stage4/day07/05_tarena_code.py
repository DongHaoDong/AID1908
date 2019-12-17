import requests

url = 'https://code.tarena.com/cn/AIDCode/sid1905/13-redis/'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).text
print(html)