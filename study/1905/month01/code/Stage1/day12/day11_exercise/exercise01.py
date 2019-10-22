"""
请用面向对象思想描述一下场景
    张无忌 教 赵敏 九阳神功
    赵敏 教 张无忌 化妆
    张无忌 上班 挣了 10000
    赵敏 上班 挣了 6000
    体会：对象区分数据的不同
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
    def teach(self,other,skill):
        print("{}教{}{}".format(self.name,other.name,skill))
    def work(self,money):
        print("{}上班挣了{}元".format(self.name,money))
zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"化妆")
zwj.work(10000)
zm.work(6000)