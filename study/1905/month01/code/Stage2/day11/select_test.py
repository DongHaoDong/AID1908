"""
test    函数实例
"""
from select import select
from socket import *
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
f = open('log.txt','r+')
print("监控IO")
rs,ws,xs = select([s],[f],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)