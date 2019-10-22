from socket import *
s = socket()
s.connect(('127.0.0.1',8888))

# 读取目标文件，循环发送
f = open('file.jpg','rb')
while True:
    # 边读边发
    data = f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()