"""
创建两个进程,分别复制一个文件的上半部分和下半部分到新的文件中
"""
from multiprocessing import Process
import os
filename = './dream.jpg'
size = os.path.getsize(filename)
fr = open(filename,'rb')
# 复制上半部分
def top():
    # fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
# 复制下半部分
def bot():
    # fr = open(filename,'rb')
    fw = open('bot.jpg','wb')
    fr.seek(size // 2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()
p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()