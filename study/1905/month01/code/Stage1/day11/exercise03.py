"""
练习定义敌人类(姓名,攻击力 10--50，血量100--200)
创建一个敌人对象，可以修改数据，读取数据
"""
class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        # self.set_hp(hp)
        self.atk = atk
        # self.set_atk(atk)
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")
e01 = Enemy("灭霸",120,40)
e01.hp = 140
print(e01.hp)