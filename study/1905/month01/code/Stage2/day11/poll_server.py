"""
poll_server.py   完成tcp并发服务
思路:IO多路复用实现并发
    建立fileno --> io对象字典用于IO查找
"""
from socket import *
from select import *
# 创建监听套接字,作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典,通过一个IO的fileno找到IO对象
# 始终跟registerIO保持一致
fdmap = {s.fileno():s}
# 关注s
p.register(s,POLLIN|POLLERR)

# 循环监控IO发生
while True:
    events = p.poll()
    # 循环遍历列表,查看哪个IO就绪,进行处理
    for fd,event in events:
        # 区分哪个IO就绪
        if fd == s.fileno():
            c, address = fdmap[fd].accept()
            print("Connect from",address)
            # 关注客户端链接套接字
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  # 判断是否为POLLIN就绪,再处理
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)   # 取消关注
                fdmap[fd].close()
                del fdmap[fd] # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b'OK')
