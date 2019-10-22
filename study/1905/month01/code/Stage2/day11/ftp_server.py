"""
ftp 文件服务器,服务端
env:python3.6
多进程/线程并发 socket
"""
from socket import *
from threading import Thread
import sys,os
import time
# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDRESS = (HOST,PORT)
FTP = "/home/tarena/FTP/"   # 文件库位置


# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表,下载,上传,退出处理
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 拼接文件
        filelist = ""
        for file in files:
            if file[0] != "." and os.path.isfile(FTP+file):
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_get(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            # 打开失败文件不存在
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()


    # 循环接收请求,分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return # 线程结束
            elif data == "L":
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)

# 搭建网络服务端模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDRESS)
    s.listen(5)
    print("Listen the port 8888....")
    # 循环等待客户端链接
    while True:
        try:
            c, address = s.accept()
            print("Connect from", address)
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue
        # 创建线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start()  # 运行run

if __name__ == "__main__":
    main()