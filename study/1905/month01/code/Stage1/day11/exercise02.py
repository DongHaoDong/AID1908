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
    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")
    atk = property(get_atk,set_atk)
    def get_hp(self):
        return self.__hp
    def set_hp(self,value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")
    hp = property(get_hp,set_hp)
e01 = Enemy("灭霸",120,40)
e01.hp = 140
print(e01.get_hp())