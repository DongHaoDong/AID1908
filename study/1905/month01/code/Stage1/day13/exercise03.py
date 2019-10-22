"""
    手雷炸了，可能伤害敌人/玩家生命，还可能伤害未知事物
    要求增加新事物不影响手雷
    体会：继承的作用
            多态的体现
            设计原则
                开闭原则
                单一职责
                依赖倒置
    画出设计图
"""
class Grenade:
    def __init__(self,atk):
        self.atk = atk
    def explode(self,damage_target):
        if isinstance(damage_target,Damageable):
            print("爆炸")
            damage_target.damage(self.atk)
        elif not isinstance(damage_target,Damageable):
            raise ValueError("不是Damageable子类")
class Damageable:
    """
    可以受伤
    """
    def damage(self,value):
        # 如果子类不重写则报异常
        raise NotImplementedError()
# ----------------------------------------
class Player(Damageable):
    def __init__(self,hp):
        self.hp = hp
    def damage(self,value):
        self.hp -= value
        print("玩家受伤了")
        print("碎屏")
class Enemy(Damageable):
    def __init__(self,hp):
        self.hp = hp
    def damage(self,value):
        self.hp -= value
        print("敌人受伤了")
        print("头顶爆字")
g01 = Grenade(100)
e01 = Enemy(200)
p01 = Player(300)
g01.explode(p01)