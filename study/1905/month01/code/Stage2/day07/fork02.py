"""
fork02.py fork进程创建演示2
"""
import os
from time import sleep
print("=============================")
a = 1
# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    print("The new process")
    print("a=",a)
    a = 10000
# 父进程执行部分
else:
    sleep(1)
    print("The old process")
    print("a:",a)
# 父子进程都会执行
print("All a->",a)