"""
生产者-生产url地址
"""
import redis
import time
import random
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# 生产者生产url地址
for page in range(67):
    url = 'http://app.mi.com/category/2#page={}'.format(page)
    r.lpush('xiaomi:spider',url)
    time.sleep(random.randint(1,3))
