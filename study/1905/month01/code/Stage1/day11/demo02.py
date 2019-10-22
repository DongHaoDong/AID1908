"""
    使用property(读取方法，写入方法)封装变量
"""
# 使用方法封装变量
class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        # 本质：障眼法(实际将变量名改为:_类名__变量名)
        # self.set_age(age)
        self.age = age
        # self.set_weight(weight)
        self.weight = weight
    # 提供公开的读方法
    def get_age(self):
        return self.__age
    # 提供公开的写方法
    def set_age(self,value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")
    # 属性 拦截对age变量的读与写操作
    age = property(get_age, set_age)
    # 提供公开的读方法
    def get_weight(self):
        return self.__weight
    # 提供公开的写方法
    def set_weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")
    # 属性 拦截对weight变量的读与写操作
    weight = property(get_weight, set_age)
w01 = Wife("婉儿公主",30,50)
# w01.set_age(25)
w01.age = 25
print(w01.get_age())
w01.weight = 45
print(w01.get_weight)