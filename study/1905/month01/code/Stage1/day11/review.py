"""
    day10 复习
    类和对象
        类：抽象    向量 class Vector2    str    int  list
        对象：具体   1,2 Vector2(1,2)     "a"    1   [1,2]
        之间的区别:  类与类行为不同
                    对象与对象数据不同
                    Vector2(1,2)    Vector2(3,4)
                    同一个类型的多个对象，数据不同(1,2/3,4),行为(求方向,球大小)相同
        类成员:
            实例：对象的数据(变量),对象的行为(方法)
            类：类的数据(变量),类的行为(方法)
                可以被所有对象共同操作的数据
            静态方法：
                实例方法操作者实例变量，表示个体的行为
                类方法操作类变量，表示大家行为
                静态方法不能操作数据，表示为函数都可以
"""
# ---------------------实例------------------------
class MyClass01:
    def __init__(self,a):
        # 实例变量
        self.a = a

    # 实例方法
    def print_self(self):
        # 可以操作实例变量
        print(self.a)
# 通过对象访问
m01 = MyClass01(100)
m01.b = 1

m02 = MyClass01(100)
print(m02.b)
print(m02.a)
# ---------------------类------------------------
class MyClass02:
    # 实例变量
    a = None
    # 类方法
    @classmethod    # 自动传入当前方法的参数是类，不是对象
    def print_self(cls):
        # 可以操作类变量
        print(cls.a)
# 通过类名访问
print(MyClass02.a)
MyClass02.print_self()
# ---------------------不建议的访问方式------------------------
# 访问实例方法，还可以通过类
MyClass01.print_self(m01)   # 也必须传递对象

# 访问类成员，可以通过对象
m03 = MyClass02()
print(m03.a)
print(m03.print_self())