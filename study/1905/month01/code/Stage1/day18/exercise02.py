"""
    练习1
    在list_helper.py中增加通用的求和方法
    案例：计算敌人列表中所有敌人的总血量
    案例：计算敌人列表中所有敌人的总攻击力
    案例：计算敌人列表中所有敌人的总防御力
    步骤
    实现具体功能/提取变化/提取不变/组合
    练习2
    在list_helper.py中增加通用的筛选方法
    案例：获取敌人列表中所有敌人的名称
    案例：获取敌人列表中所有敌人的攻击力
    案例：获取敌人列表中所有敌人的名称和血量
    练习3
    在list_helper.py中增加通用的获取最大值方法
    案例：获取敌人列表中攻击力最大的敌人
    案例：获取敌人列表中防御力最大的敌人
    案例：获取敌人列表中血量最大的敌人
    练习4
    在list_helper.py中增加通用的升序排列方法
    案例：将敌人列表按照攻击力进行升序排列
    案例：将敌人列表按照防御力进行升序排列
    案例：将敌人列表按照血量进行升序排列

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
# 练习1
"""
# 实现具体功能
def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.atk
    return sum_value
def sum02():
    sum_value = 0
    for item in list01:
        sum_value += item.hp
    return sum_value
def sum03():
    sum_value = 0
    for item in list01:
        sum_value += item.defense
    return sum_value
# 提取变化的过程
def handle01(item):
    return item.atk
def handle02(item):
    return item.hp
def handle03(item):
    return item.defense
# 提取不变的过程
def sum(function_handle):
    sum_value = 0
    for item in list01:
        # sum_value += item.defense
        # sum_value += handle01(item)
        sum_value += function_handle(item)
    return sum_value
print(sum(handle01))
"""
print(ListHelper.sum(list01,lambda item:item.hp))
# 练习2
"""
def select01():
    result = []
    for item in list01:
        result.append(item.name)
    return result
def select02():
    result = []
    for item in list01:
        result.append(item.atk)
    return result
def select03():
    result = []
    for item in list01:
        result.append((item.name,item.hp))
    return result
def handle01(item):
    return item.name
def handle02(item):
    return item.atk
def handle03(item):
    return (item.name,item.hp)
# def select(function_handle):
#     result = []
#     for item in list01:
#         # result.append((item.name, item.hp))
#         # result.append(handle03(item))
#         function_handle(item)
#     return result
def select(function_handle):
    for item in list01:
        yield function_handle(item)
for item in select(handle01):
    print(item)
"""
for item in ListHelper.select(list01,lambda item:(item.name,item.hp)):
    print(item)
# 练习3
"""
def max1():
    max_value = list01[0]
    for index in range(1,len(list01)):
        if max_value.atk < list01[index].atk:
            max_value = list01[index]
        return max_value
def max02():
    max_value = list01[0]
    for index in range(1,len(list01)):
        if max_value.defense < list01[index].defense:
            max_value = list01[index]
        return max_value
def max03():
    max_value = list01[0]
    for index in range(1,len(list01)):
        if max_value.hp < list01[index].hp:
            max_value = list01[index]
        return max_value
def handle01(item):
    return item.atk
def handle02(item):
    return item.defense
def handle03(item):
    return item.hp
def get_max(function_handle):
    max_value = list01[0]
    for index in range(1,len(list01)):
        # if max_value.hp < list01[index].hp:
        # if handle03(max_value) < handle03(list01[index]):
        if function_handle(max_value) < function_handle(list01[index]):
            max_value = list01[index]
    return max_value
print(get_max(handle03))
"""
print(ListHelper.get_max(list01,lambda item:item.hp))
# 练习4
"""
def order_by01():
    # 取出前几个数据
    for row in range(len(list01) - 1):
        # 与后面进行对比
        for col in range(row + 1,len(list01)):
            if list01[row].atk > list01[col].atk:
                list01[row],list01[col] = list01[col],list01[row]
def order_by02():
    # 取出前几个数据
    for row in range(len(list01) - 1):
        # 与后面进行对比
        for col in range(row + 1, len(list01)):
            if list01[row].defense > list01[col].defense:
                list01[row], list01[col] = list01[col], list01[row]
def order_by03():
    # 取出前几个数据
    for row in range(len(list01) - 1):
        # 与后面进行对比
        for col in range(row + 1, len(list01)):
            if list01[row].hp > list01[col].hp:
                list01[row], list01[col] = list01[col], list01[row]
def handle01(item):
    return item.atk
def handle02(item):
    return item.defense
def handle03(item):
    return item.hp
def order_by(function_handle):
    # 取出前几个数据
    for row in range(len(list01) - 1):
        # 与后面进行对比
        for col in range(row + 1, len(list01)):
            # if list01[row].hp > list01[col].hp:
            # if handle03(list01[row]) > handle03(list01[col]):
            if function_handle(list01[row]) > function_handle(list01[col]):
                list01[row], list01[col] = list01[col], list01[row]
for item in list01:
    print(item)
order_by(handle02)
print("-----------------------------------------------------")
for item in list01:
    print(item)
"""
ListHelper.order_by(list01,lambda item:item.defense)
for item in list01:
    print(item)