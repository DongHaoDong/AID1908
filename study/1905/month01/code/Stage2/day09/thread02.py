"""
thread02.py  线程函数参数演示
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("线程函数参数")
    sleep(sec)
    print("{}执行完毕".format(name))
# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={'name':'T{}'.format(i)})
    jobs.append(t)  # 存储线程对象
    t.start()

for i in jobs:
    i.join()