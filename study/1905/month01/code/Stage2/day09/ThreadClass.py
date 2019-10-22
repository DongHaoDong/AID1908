"""
ThreadClass.py     自定义线程类
"""
from threading import Thread
# 自定义线程类
class myThread(Thread):
    # 重写父类init
    def __init__(self,*args,**kwargs):
        self.attr = args[0]
        super().__init__()  # 加载父类init
    # 假设需要很多步骤完成功能
    def f1(self):
        print("step 1")
    def f2(self):
        print("step 1")
    # 重写run逻辑调用
    def run(self):
        self.f1()
        self.f2()
t = myThread('abc')
t.start()
t.join()