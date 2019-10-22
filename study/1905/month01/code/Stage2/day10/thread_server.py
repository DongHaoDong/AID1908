"""
thread_server.py    基于threading的网络并发
1.创建套接字
2.循环等待客户端链接
3.创建线程处理客户端请求
4.客户端退出销毁对应线程
"""
from socket import *
from threading import Thread
import sys

# 设置全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDRESS = (HOST,PORT)

# 处理客户端具体请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDRESS)
s.listen(5)
print("Listen the port 8888....")
# 循环等待客户端链接
while True:
    try:
        c, address = s.accept()
        print("Connect from", address)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue
    # 创建线程处理请求
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()
