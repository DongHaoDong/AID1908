# 服务端提供逻辑和数据处理
from socket import *
def find_word(word):
    f = open('dict.txt')

    # 每次获取一行
    for line in f:
        w = line.split(' ')[0]
        # 如果便利的单词已经大于word就结束查找
        if w > word:
            f.close()
            return "没有找到该单词"
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return "没找到该单词"

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_address = ('0.0.0.0',8888)
sockfd.bind(server_address)

# 收发消息
while True:
    # data就是接到的单词
    data,address = sockfd.recvfrom(1024)
    # 查单词
    result = find_word(data.decode())
    sockfd.sendto(result.encode(),address)
# 关闭套接字
sockfd.close()