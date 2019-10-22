"""
http请求响应测试
"""
from socket import *
# http使用tcp传输
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)
c,address = s.accept()
print("Connect from",address)
data = c.recv(4096) # 接收http请求
print(data)
s.close()
s.close()
