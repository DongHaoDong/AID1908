from socket import *

s = socket()
s.bind(("127.0.0.1",8888))
s.listen(3)

c,address = s.accept()
print("Connect from",address)

# 接收文件思路：1.wb写打开新文件 2.recv 内容 write文件

# 打开文件
f = open('dream.jpg','wb')

# 循环接收写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()