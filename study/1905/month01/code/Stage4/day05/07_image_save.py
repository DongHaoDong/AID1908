'''
非结构化数据的抓取
'''
from urllib import request
url = 'https://p0.meituan.net/movie/2fa54840eb3bb5c3decf0e28cc1f894c2067576.jpg'
res = request.urlopen(url)
html = res.read()
with open('误杀.jpg','wb') as f:
    f.write(html)
# os模块的使用
import os
dicrectory = 'C:/Users/习惯就好/Desktop/gitproject/study/1905/month01/code/Stage4/day05'
if not os.path.exists(dicrectory):
    os.makedirs(dicrectory)