from socket import *
import struct

# 和客户端一致
st = struct.Struct("i32sif")

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 打开文件
f = open('student.txt','a')

while True:
    data,address = s.recvfrom(1024)
    # (1,b'Lily',14,92.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d     %-10s     %d     %.1f\n"%data
    f.write(info)
    f.flush()

