"""
    内置高阶函数
    练习：内置高阶函数
    1.([1,1,1],[2,2],[3,3,3，3])
        获取元组中，列表长度最大的列表
    2.根据敌人列表，获取所有敌人的姓名、血量、攻击力
    3.在敌人列表中获取攻击力大于100的所有活人
    4.根据防御力对敌人列表进行排序
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

# 1.filter:根据条件筛选可迭代对象中的元素，返回值为新可迭代对象
# 需求:获取所有死人
for item in ListHelper.find_all(list01,lambda item:item.hp == 0):
    print(item)
print("==========================================")
result = filter(lambda item:item.hp == 0,list01)
for item in result:
    print(item)
# 2.通用的筛选方法
# 需求：获取所有敌人的姓名
for item in ListHelper.select(list01,lambda item:item.name):
    print(item)
print("==========================================")
result = map(lambda item:item.name,list01)
for item in result:
    print(item)
# 3.max:获取最大值
# 需求：获取血量最大的敌人
# print(ListHelper.get_max(list01,lambda item:item.hp))
# print(max(list01,key = lambda item:item.hp))
# 5.
# 需求：根据攻击力升序排列
# 内部直接修改列表，使用时无需通过返回值获取数据
# ListHelper.order_by(list01,lambda item:item.atk)
# for item in list01:
#     print(item)
# 内部返回新列表，使用时必须获取返回值
# result = sorted(list01,key = lambda item:item.atk)
# for item in result:
#     print(item)
# 支持降序排序
result = sorted(list01,key = lambda item:item.defense,reverse=True)
for item in result:
    print(item)