"""
file_write.py
文件写操作演示
"""
# 打开文件
f = open('test.txt','a')
# f = open('images.jpg','ab')
# 写操作
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥".encode())

# 将列表写入 需要人为的添加换行
# l = ['hello world\n','哈哈哈\n']
f.write("董浩东")
f.close()
