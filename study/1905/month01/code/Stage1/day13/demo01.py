"""
    继承 -- 方法
        财产：钱不用孩子挣，但可以花
        皇位：江山不用孩子打，但是可以坐
        代码：子类不用写，但是可以用
"""
# 多个子类在概念上是一致的，所以抽象出一个父类
# 多个子类的共性，可以抽象到父类中
# 从设计角度讲:先有子，再有父
# 从编码角度中讲：先有父，再有子
class Person:
    def say(self):
        print("说话")
class Student(Person):
    def study(self):
        print("学习")
class Teacher(Person):
    def teach(self):
        print("讲课")
s01 = Student()
# 子类对象可以调用子类成员，也可以调用父类成员
s01.study()
s01.say()   # 父类成员

p01 = Person()
# 父类对象只可以调用父类成员，不能调用子类成员
p01.say()

t01 = Teacher()

# Python 内置函数
# 1.判断对象是否属于一个类型
# "老师对象" 是一个老师类型
print(isinstance(t01,Teacher))  # True
# "老师对象" 不是一个学生类型
print(isinstance(t01,Student))  # False
# "老师对象" 是一个人类型
print(isinstance(t01,Person))   # True
# 2.判断一个类型是否属于另一个类型
# "老师类型" 不是一个学生类型
print(issubclass(Teacher,Student))  # False
# "老师类型" 是一个人类型
print(issubclass(Teacher,Person))   # True
# "人类型" 不是一个老师类型
print(issubclass(Person,Teacher))   # False