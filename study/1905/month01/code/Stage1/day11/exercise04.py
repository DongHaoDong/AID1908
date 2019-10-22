"""
    请以面向对象的思想，描述下列场景：
        小明在招商银行取钱
"""
class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def draw_money(self,person,value):
        """
        取钱
        :param person:
        :param value:
        :return:
        """
        self.money -= value
        person.money += value
        print("{}取了{}钱".format(person.name,value))
xm = Person("小明",0)
zsyh = Bank("招商",10000)
zsyh.draw_money(xm,1000)
