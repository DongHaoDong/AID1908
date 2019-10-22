"""
    day11   复习
        封装
            数据角度：将多个变量封装到一个自定义类中。
                    优势：
                        符合人类的思考方式
                        可以将数据与对数据的操作封装在一起
            功能角度：对外提供必要的功能，隐藏实现的细节
                    DoubleListHelper.get_elements()
                    --私有化：将名称命名为以双下划线开头
                            内部修改成员名称
                    --属性：对实例变量的保护(拦截读/写操作)
                    -- __slots__:限定类创建的对象只能有固定的实例变量
            设计角度：
                分而治之：将大的需求分解为多个类，每个类负责一个职责
                变则疏之：遇到变化点单独封装为一个类
                高内聚：一个类有且只有一个发生变化的原因
                低耦合：类与类的关系松散
"""
# 封装数据
class Student01:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_self(self):
        print(self.name,self.age)
s01 = Student01("无忌哥哥",28)
# 通过对象调用实例成员
s01.name = "张无忌"
s01.print_self()

class Student02:
    def __init__(self,name,age):
        self.name = name
        self.set_name(name)
        self.age = age
        self.set_age(age)
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name = value
    def get_age(self):
        return self.__age
    def set_age(self,value):
        self.__age = value
s02 = Student02("无忌哥哥",28)
s02.name = "张无忌"

class Student03:
    def __init__(self,name,age):
        self.name = name
        # self.set_name(name)
        self.age = age
        # self.set_age(age)
    def __get_name(self):
        return self.__name
    def __set_name(self,value):
        self.__name = value
    name = property(__get_name,__set_name)
    def __get_age(self):
        return self.__age
    def __set_age(self,value):
        self.__age = value
    age = property(__get_age,__set_age)
s03 = Student03("无忌哥哥",28)
s03.name = "张无忌"
print(s03.name)

class Student04:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value
s04 = Student04("无忌哥哥",28)
s04.name = "张无忌"
print(s04.name)

class Student05:
    # 限制对象创建新实例变量
    __slots__ = ("name","age")
    def __init__(self,name,age):
        self.name = name
        self.age = age
s05 = Student05("无忌",28)
s05.name = "张无忌"
print(s05.name)

class Student06:
    __slots__ = ("__name","__age")
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value
s06 = Student06("无忌哥哥",28)
s06.name = "张无忌"
print(s04.name)

