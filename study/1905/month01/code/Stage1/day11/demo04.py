"""
    封装设计思想
        需求：老张开车去东北
"""
class Person:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    def go_to(self,str_postion,type):
        """
            去
        :param str_postion:位置
        :param type:方法
        :return:
        """
        print("{}去{}".format(self.name,str_postion))
        type.run(str_postion)
class Car:
    def run(self,str_position):
        """
            行驶
        :param str_position:位置
        :return:
        """
        print("行驶到:{}".format(str_position))
lz = Person("老张")
car = Car()
# 老张开车去东北
lz.go_to("东北",car)


