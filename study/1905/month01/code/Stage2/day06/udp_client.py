"""
udp_client.py   udp客户端流程
"""
from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 服务器地址
ADDRESS = ('127.0.0.1',8888)
# 循环收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDRESS)
    msg,address = sockfd.recvfrom(1024)
    print("From server:",msg.decode())
sockfd.close()