"""
thread01.py     线程基础使用
步骤：基本同Process
    1.封装进程函数
    2.创建线程对象
    3.启动线程
    4.回收线程
"""
import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：黄河大合唱")
    global a
    print("a = ",a)
    a = 10000
# 创建线程对象
t = threading.Thread(target=music)
t.start()   # 启动线程
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：葫芦娃")
t.join()    # 回收线程
print("a:",a)
