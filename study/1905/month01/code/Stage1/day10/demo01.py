"""
    对象内存图
"""
class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
    def print_self_info(self):
        print("{}的年龄是{},成绩是{},性别是{}".format(self.name, self.age, self.score, self.sex))

list01 = [
    Student("董浩东",21,90,"男"),
    Student("学习",21,100,"保密"),
]
