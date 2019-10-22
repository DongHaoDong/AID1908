"""
chat room
env: python3.6
socket udp & fork
"""
from socket import *
import os,sys

"""
局部变量：很多封装模块都要用或者有一定的固定含义
"""
# 服务器地址
ADDRESS = ('0.0.0.0',8888)

# 存储用户{name:address}
user = {}

# 登录
def do_login(s,name,address):
    if name in user or '管理员' in name:
        s.sendto('该用户存储在'.encode(),address)
        return
    s.sendto(b'OK', address)  # 可以进入聊天室

    # 通知其他人
    msg = "\n欢迎'{}'进入聊天室".format(name)
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = address    # 插入字典

# 聊天
def do_chat(s,name,text):
    message = "\n{}:{}".format(name,text)
    for i in user:
        # 刨除其本人
        if i != name:
            s.sendto(message.encode(),user[i])

# 退出
def do_quit(s,name):
    message = "\n{}退出聊天室".format(name)
    for i in user:
        if i != name:   # 其他人
            s.sendto(message.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    del user[name]  # 删除用户

# 处理请求
def do_request(s):
    while True:
        data,address = s.recvfrom(1024)
        temp = data.decode().split(' ')     # 拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L 进入      C 聊天    Q 退出
        if temp[0] == 'L':
            do_login(s,temp[1],address)  # 执行具体工作
        elif temp[0] == 'C':
            text = ' '.join(temp[2:])
            do_chat(s,temp[1],text)
        elif temp[0] == 'Q':
            do_quit(s,temp[1])

# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDRESS)
    pid = os.fork()
    if pid == 0:    # 子进程处理管理员消息
        while True:
            message = input("管理员消息：")
            message = "C 管理员 "+message
            s.sendto(message.encode(),ADDRESS)
    else:
        # 请求处理函数
        do_request(s)

main()