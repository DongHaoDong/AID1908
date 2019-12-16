'''
模拟30个并发，向8000和8001端口随机发送请求
'''
from threading import Thread
import random
import requests

# 线程事件函数，功能:随机向8000或8001发送请求
def get_request():
    url1 = 'http://127.0.0.1:8000/test/'
    url2 = 'http://127.0.0.1:8001/test/'
    url = random.choice([url1,url2])
    # 发送请求
    requests.get(url)

t_list = []
for i in range(30):
    t = Thread(target=get_request)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()


