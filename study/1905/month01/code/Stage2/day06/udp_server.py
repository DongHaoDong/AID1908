"""
upd_server.py udp套接字服务器端流程
"""
from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_address = ('127.0.0.1',8888)
sockfd.bind(server_address)

# 收发消息
while True:
    data,address = sockfd.recvfrom(1024)
    print("收到消息：",data.decode())
    sockfd.sendto(b'Thanks',address)
# 关闭套接字
sockfd.close()