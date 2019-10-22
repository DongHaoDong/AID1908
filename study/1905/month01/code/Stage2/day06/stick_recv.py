"""
粘包演示
"""
from socket import *
from time import sleep

# 创建tcp套接字
sockfd = socket()

# 绑定地址
sockfd.bind(('0.0.0.0',8889))

# 设置监听
sockfd.listen(5)

connnfd,address = sockfd.accept()

while True:
    sleep(1)
    data = connnfd.recv(1024)
    print(data.decode())