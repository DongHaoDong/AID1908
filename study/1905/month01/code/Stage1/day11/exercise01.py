"""
练习定义敌人类(姓名,攻击力 10--50，血量100--200)
创建一个敌人对象，可以修改数据，读取数据
"""
class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        # self.__hp = hp
        self.set_hp(hp)
        # self.__atk = atk
        self.set_atk(atk)
    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")
    def get_hp(self):
        return self.__hp
    def set_hp(self,value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")
e01 = Enemy("灭霸",25,120)
# e01.set_atk(20)
print(e01.get_atk())