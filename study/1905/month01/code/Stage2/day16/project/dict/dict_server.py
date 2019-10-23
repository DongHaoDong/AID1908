"""
dict 服务端

功能：业务逻辑处理
模型：多进程 tcp 并发
"""
from socket import *
from multiprocessing import Process
import signal
import sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDRESS = (HOST, PORT)


# 接收客户端请求，分配处理函数
def request(c):
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)


# 搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDRESS)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端连接
    print("Listen the port 8000")
    while True:
        try:
            c, address = s.accept()
            print("Connect from", address)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue
        # 为客户端创建子进程
        p = Process(target=request, args=(c,))
        p.daemon = True
        p.start()


if __name__ == "__main__":
    main()
