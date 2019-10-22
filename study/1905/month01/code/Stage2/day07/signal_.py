"""
信号处理僵尸
"""
import os,sys
import signal
# 子进程退出时父进程忽略退出行为，子进程由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2) # 子进程退出状态×256
else:
    while True:     # 父进程不退出
        pass
