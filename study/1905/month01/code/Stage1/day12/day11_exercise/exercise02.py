"""
请用面向对象思想，描述以下场景
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可以死亡(掉装备，加分)
    敌人(攻击力)攻击玩家(血量)，玩家受伤后(掉血/碎屏)(游戏结束)
    体会：类区分行为的不同
"""
class Player:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def attack(self,other):
        # 打的逻辑
        print("玩家攻击敌人")
        # 通过敌人对象地址，调用实例方法
        other.damage(self.atk)
    def damage(self,value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死喽")
        print("游戏结束")


class Enemy:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    def damage(self,value):
        # 受伤的逻辑
        print("敌人受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.__death()
    def attack(self,other):
        print("敌人攻击玩家")
        other.damage(self.atk)
    # 私有的死亡的方法
    def __death(self):
        # 死亡的逻辑
        print("死亡")
        print("掉装备")
        print("加分")
p01 = Player(1000,100)
e01 = Enemy(200,10)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)