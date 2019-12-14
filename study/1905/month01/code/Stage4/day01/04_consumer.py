"""
消费者
"""
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

while True:
    # url:(b'xiaomi:spider',b'http://app.mi.com/category/2#page=0')
    url = r.brpop('xiaomi:spider',4)
    if url:
        print('正在抓取',url[1].decode())
    else:
        print('抓取结束')
        break
