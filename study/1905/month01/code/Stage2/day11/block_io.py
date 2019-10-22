"""
block_io.py
socket 套接字非阻塞实例
"""
from socket import *
from time import ctime,sleep
# 日志文件
f = open('log.txt','a+')
# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)
# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)
while True:
    print("Waiting for connect....")
    # 没有客户端连接每隔3秒写一条日志
    try:
        connfd,address = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        sleep(3)
        f.write("{} : {}\n".format(ctime(),e))
        f.flush()
    else:
        print("Connect from",address)
        data = connfd.recv(1024).decode()
        print(data)