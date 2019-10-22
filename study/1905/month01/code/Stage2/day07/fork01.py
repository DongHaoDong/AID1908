"""
fork01.py fork进程创建演示
"""
import os
from time import sleep
# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    sleep(3)
    print("The new process")
# 父进程执行部分
else:
    sleep(4)
    print("The old process")
# 父子进程都会执行
print("Fork test over")
