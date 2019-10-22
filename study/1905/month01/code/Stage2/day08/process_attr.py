"""
进程对象属性
"""
from multiprocessing import Process
import time
def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)
p = Process(target=tm,name='dream')
p.daemon = True # 父进程退出子进程也随之退出
p.start()
time.sleep(1)
print("Name:",p.name)   # 进程名称
print("PID:",p.pid) # 对应子进程PID
print("is alive:",p.is_alive()) #进程是否在生命周期


