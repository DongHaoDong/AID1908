"""
    定义对象计数器
    定义老婆类，创建3个老婆对象
"""
class Wife:
    count = 0
    @classmethod
    def print_count(cls):
        print(cls.count)
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Wife.count += 1
w01 =  Wife("如玉",25)
w02 =  Wife("婉儿",23)
w03 =  Wife("九儿",21)
Wife.print_count()