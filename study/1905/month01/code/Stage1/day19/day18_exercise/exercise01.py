"""

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

# print(ListHelper.get_min(list01,lambda item:item.hp))
# ListHelper.order_by_descending(list01,lambda item:item.hp)
# for item in list01:
#     print(item)
"""
# 案例：在敌人列表中，删除所有死人
def del01():
    # 3,2,1,0
    for index in range(len(list01)-1,-1,-1):
        if list01[index].hp == 0:
            del list01[index]
# 案例：在敌人列表中，删除攻击力小于50的所有敌人
def del02():
    # 3,2,1,0
    for index in range(len(list01)-1,-1,-1):
        if list01[index].atk < 50:
            del list01[index]
# 案例：在敌人列表中，删除防御力大于100的所有敌人
def del03():
    # 3,2,1,0
    for index in range(len(list01)-1,-1,-1):
        if list01[index].defense > 100:
            del list01[index]

def condition01(item):
    return item.hp == 0
def condition02(item):
    return item.atk < 50
def condition03(item):
    return item.defense > 100
def delete_all(function_condition):
    # 使用正向索引倒序删除
    # 3,2,1,0
    for index in range(len(list01)-1,-1,-1):
        # if list01[index].defense > 100:
        # if condition03(list01[index]):
        if function_condition(list01[index]):
            del list01[index]
delete_all(condition01)
for item in list01:
    print(item)
"""
ListHelper.delete_all(list01,lambda item:item.hp == 0)
for item in list01:
    print(item)