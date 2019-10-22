"""
    继承 -- 变量
"""
class Person:
    def __init__(self,name):
        self.name = name
"""
class Student(Person):
    # 子类若没有构造函数，使用父类的构造函数
    pass
s01 = Student()
print(s01.name)
"""
class Student(Person):
    # 子类若具有构造函数，则必须先调用父类的构造函数
    def __init__(self,name,score):
        super().__init__(name)
        self.score = score
s01 = Student("张三",100)
print(s01.score)
print(s01.name)