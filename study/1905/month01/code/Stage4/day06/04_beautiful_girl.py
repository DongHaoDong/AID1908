import requests

url = 'http://i.shangc.net/2017/0627/20170627034048269.jpg'
headers = {'User-Agent':'Mozilla/5.0'}
html = requests.get(url=url,headers=headers).content
with open('花千骨.jpg','wb') as f:
    f.write(html)
