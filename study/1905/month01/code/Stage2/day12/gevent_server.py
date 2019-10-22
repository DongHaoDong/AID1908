"""
gevent server基于携程的TCP并发
思路:
1.将每个客户端的处理设置为携程函数
2.让socket模块下的阻塞可以触发协成跳转
"""
import gevent
from gevent import monkey
monkey.patch_all()  # 执行脚本,修改socket
from socket import *

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 循环接收客户端链接
while True:
    c,address = s.accept()
    print("Connect from",address)
    # handle(c) # 处理具体的客户端请求
    gevent.spawn(handle(c)) # 携程方案