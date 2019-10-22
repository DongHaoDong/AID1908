"""
3.定义敌人类(姓名,攻击类,防御力,血量)
    创建敌人列表,使用list_helper实现下列功能
    (1)查找姓名是"灭霸"的敌人
    (2)查找攻击力大于10的所有敌人
    (3)查找活的敌人数量
4.在list_helper中增加判断是否存在某个对象的方法
    案例：判断敌人列表中是否存在"成昆",返回值"成昆"
    案例：判断敌人列表中攻击力小于5或者防御力小于10的敌人
    步骤
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list_helper.py中
    体会函数式编程的思想(封装，继承，多变)
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
# 查找姓名是"灭霸"的敌人
result = ListHelper.find_single(list01,lambda item:item.name == "灭霸")
print(result)
# 查找攻击力大于10的所有敌人
generater_result = ListHelper.find_all(list01,lambda item:item.atk > 10)
# for item in generater_result:
#     print(item)

# 生成器 --> 惰性操作
# 优势：节省时间
# 缺点：获取结果不灵活(不能使用索引/切片访问结果)
# 解决：惰性操作 --> 立即操作
list_result = list(generater_result)
for item in list_result[:2]:
    print(item)

# 查找活的敌人
for item in ListHelper.find_all(list_result,lambda item:item.hp > 0):
    print(item)
# 查找活的敌人数量
print(ListHelper.get_count(list_result,lambda item:item.hp > 0))

# 2.判断是否存在某个对象的方法
# 案例1:判断敌人列表中是否存在"成昆"
# 案例2:判断敌人列表中攻击力小于5或者防御力小于10的敌人

"""
def is_exists01():
    for item in list01:
        if item.name == "成昆":
            return True
    return False
def is_exists02():
    for item in list01:
        if item.atk < 5 or item.defense < 10:
            return True
    return False
def condition01(item):
    return item.name == "成昆"
def condition02(item):
    return item.atk < 5 or item.defense < 10

def is_exists(function_condition):
    for item in list01:
        # if item.name == "成昆":
        # if condition01(item)
        if function_condition(item):
            return True
    return False
print(is_exists(condition02))
"""
print(ListHelper.is_exists(list01,lambda item:item.name == "成昆"))