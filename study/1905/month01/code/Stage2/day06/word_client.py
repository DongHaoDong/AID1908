# 发送请求，展示请求结果
from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 服务器地址
ADDRESS = ('127.0.0.1',8888)
# 循环收发消息
while True:
    data = input("Word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDRESS)    # 发送单词
    msg,address = sockfd.recvfrom(1024)     # 单词解释
    print("From server:",msg.decode())
sockfd.close()