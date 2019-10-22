"""
gevent 携程模块实例
"""
import gevent
from gevent import monkey
monkey.patch_time()
from time import sleep

# 携程函数
def fun01(a,b):
    print("Running fun ...",a,b)
    sleep(2)
    print("fun again")

def fun02():
    print("Running fun2 ...")
    sleep(3)
    print("fun2 again")

# 生成携程对象
g01 = gevent.spawn(fun01,1,2)
g02 = gevent.spawn(fun02)
# gevent.sleep(5)
gevent.joinall([g01,g02])   # 阻塞等待g01,g02两个协程执行完毕