"""
    使用属性property，封装变量
"""
# 使用方法封装变量
class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    @property
    def age(self):
        return self.__age
    @age.setter  # 只负责拦截写入
    def age(self,value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")
    @property   # 创建property对象，只负责拦截读取
    def weight(self):
        return self.__weight
    @weight.setter  # 提供公开的写方法
    def weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")

w01 = Wife("婉儿公主",30,50)
w01.age = 25
print(w01.age)
w01.weight = 45
print(w01.weight)