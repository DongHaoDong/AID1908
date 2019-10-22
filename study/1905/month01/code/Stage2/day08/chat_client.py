"""
chat room 客户端
发送请求,展示结果
"""
from socket import *
import os,sys
# 服务器地址
ADDRESS = ('127.0.0.1',8888)

# 发送消息
def send_message(s,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            message = 'Q ' + name
            s.sendto(message.encode(),ADDRESS)
            sys.exit("退出聊天室")
        message = 'C {} {}'.format(name,text)
        s.sendto(message.encode(),ADDRESS)

# 接受消息
def receive_message(s):
    while True:
        try:
            data,address = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到EXIT退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + '\n发言：',end='')

# 客户端启用函数
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名：")
        message = 'L ' + name
        s.sendto(message.encode(), ADDRESS)
        # 接收反馈
        data,address = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_message(s,name)  # 子进程负责消息发送
    else:
        receive_message(s)   # 子进程负责消息接收

main()