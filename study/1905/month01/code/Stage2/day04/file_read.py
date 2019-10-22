"""
file_read.py
文件读取演示
"""
# 打开文件
f = open('test.txt','r')
# read循环读取
# while True:
#     # 读到文件结尾返回空字符串
#     data = f.read(100)  # 每次最多读100个字符
#     if not data:    # 读到结尾跳出循环
#         break
#     print(data)

# 读取一行内容
# data = f.readline(10)   # 读取前10个字符
# print(data)
# data = f.readline()     # 读完第一行剩余内容
# print(data)

# 将内容读取为列表，每行为列表一个元素
# data = f.readlines(18)    # 前18个字节所在的行作为读取对象
# print(data)

# f为可迭代对象
for line in f:
    print(line)     # 每次迭代到一行内容
# 关闭
f.close()