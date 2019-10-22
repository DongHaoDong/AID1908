"""
array.py    共享内存放一组数据
"""
from multiprocessing import Process, Array
# 创建共享内存
# shm = Array('i',[1,2,3,4])
# shm = Array('i',5)  # 初始化开辟5个整形空间
shm = Array('c',b'hello')   # 字节串
def fun():
    # array创建共享内存对象可迭代
    for i in shm:
        print(i)
    shm[0] = b'H'   # 修改共享内存

p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)
print(shm.value)    # 打印字节串