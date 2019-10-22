from socket import *
from time import sleep

# 创建tcp套接字
sockfd = socket()     # 使用默认参数-->tcp套接字

# 连接服务器
server_address = ('127.0.0.1',8889)     # 服务端地址
sockfd.connect(server_address)

while True:
    sleep(0.3)
    sockfd.send(b"msg")

