"""
进程池练习
"""
from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件
def worker(message):
    sleep(2)
    print(ctime(),"--",message)

# 创建进城池
pool = Pool(8)

# 向进城池队列添加事件
for i in range(10):
    message = "Tedu {}".format(i)
    pool.apply(func=worker,args=(message,))
# 关闭进程池
pool.close()
# 回收进城池
pool.join()