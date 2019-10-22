"""
queue_01.py     消息队列演示
之一：消息队列符合先进先出原则
"""
from multiprocessing import *
from time import sleep
from random import randint
# 创建消息队列
q = Queue(5)

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)
    q.put(randint(1,16))

def request():
    l = []
    for i in range(6):
        l.append(q.get())
    l.sort()
    l.append(q.get())
    print(l)
p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()