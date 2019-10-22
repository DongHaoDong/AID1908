"""
测试用例
"""
# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1
# IO
def io():
    write()
    read()
def write():
    f = open('test01','w')
    for i in range(1800000):
        f.write("Hello World\n")
    f.close()
def read():
    f = open('test01')
    lines = f.readline()
    f.close()