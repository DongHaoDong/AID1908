"""
fork_server.py 基于fork的多进程并发
重点代码
1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建新的进程处理客户端请求
4.原进程继续等待其他客户端连接
5.如果客户端退出，则销毁对应的进程
"""
from socket import *
import os
import signal
# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDRESS = (HOST,PORT)

# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDRESS)
s.listen(5)
# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")

while True:
    # 循环处理客户端链接
    try:
        c,address = s.accept()
        print("Connect from",address)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c) # 处理具体事物
        os._exit(0) # 子进程销毁
    # 无论父进程还是fork出错都要回去继续处理链接
    else:
        c.close()   # 父进程无需和客户端通信