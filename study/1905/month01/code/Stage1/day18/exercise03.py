"""
内置高阶函数
    练习：内置高阶函数
    1.([1,1,1],[2,2],[3,3,3,3])
        获取元组中，列表长度最大的列表
    2.根据敌人列表，获取所有敌人的姓名、血量、攻击力
    3.在敌人列表中获取攻击力大于100的所有活人
    4.根据防御力对敌人列表进行降序排序
"""
from common.list_helper import *
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    def __str__(self):
        return "{}--{}--{}--{}".format(self.name,self.hp,self.atk,self.defense)

list01 = [
    Enemy("玄冥二老",86,120,58),
    Enemy("成昆",0,100,5),
    Enemy("谢逊",120,130,60),
    Enemy("灭霸",0,1309,690),
]
# 1.获取元组中，列表长度最大的列表
tuple01 = ([1,1,1],[2,2],[3,3,3,3])
print(max(tuple01,key = lambda item:len(item)))
# 建议：改写之前的练习day17/exercise02.py,实现完整的my_zip.py
# 2.根据敌人列表，获取所有敌人的姓名、血量、攻击力
result = map(lambda item:(item.name,item.hp,item.atk),list01)
for item in result:
    print(item)
# 3.在敌人列表中获取攻击力大于100的所有活人
result = filter(lambda item:item.atk > 100 and item.hp > 0,list01)
for item in result:
    print(item)
# 4.根据防御力对敌人列表进行降序排序
result = sorted(list01,key=lambda item:item.defense,reverse=True)
for item in result:
    print(item)