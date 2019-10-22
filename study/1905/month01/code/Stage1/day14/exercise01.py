"""
    练习:创建Enemy类对象，将打印打印在控制台中
    克隆Enemy类对象,体会克隆对象变量的改变不影响原对象
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    def __str__(self):
        return "%s---%d---%d---%d"%(self.name,self.hp,self.atk,self.defense)
    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)
e01 = Enemy("张三",100,10,5)
print(e01)
e02 = eval(repr(e01))
e02.name = "老三"
print(e02)
