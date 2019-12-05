"""
将文件赋值一份
思路：一边读取一个文件内容，然后将其写入一个新文件中
"""
# 输入文件名
filename = input("File:")
try:
    fr = open(filename,'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open('images.jpg','wb')  # 二进制写入
    # 循环读取直至最后
    while True:
        data = fr.read(1024)
        if not data:    # 文件结束
            break
        fw.write(data)  # 将读取内容写入
    fr.close()
    fw.close()
