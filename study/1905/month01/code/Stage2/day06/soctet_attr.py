"""
套接字属性介绍
"""
from socket import *

# 创建套接字
s = socket()
s.bind(("127.0.0.1",8888))
s.listen(3)
c,address=s.accept()

print("地址类型：",s.family)
print("套接字类型：",s.type)
print("绑定地址：",s.getsockname())
print("文件描述符：",s.fileno())
# 连接套接字调用 结果同accept返回的address
print("连接端地址：",c.getpeername())
