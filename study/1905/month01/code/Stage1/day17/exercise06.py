"""
测试通用模块list_helper.py
"""
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
    def __str__(self):
        return "技能数据是：{},{},{},{}".format(self.id,self.name,self.atk_ratio,self.duration)

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]

def condition01(item):
   return item.atk_ratio > 6
def condition02(item):
   return 4 <= item.duration <= 11
def condition03(item):
   return len(item.name) > 4 and item.duration < 6
from common.list_helper import *
generate01 = ListHelper.find_all(list_skill,condition01)
for item in generate01:
    print(item)

# 练习：在list_helper.py中，定义通用的查找满足条件的单个对象
# 案例：查找名称是"葵花宝典"的技能
# 案例：查找编号是101的技能
# 案例：查找持续时间大于0的技能
# 建议
# 1.先将所有功能实现
# 2.封装变化(将变化点单独定义为函数)
#   定义不变的函数
# 3.将不变的函数转移到list_helper.py中
# 4.在当前模块中测试
"""
def find01():
    for item in list_skill:
        if item.name == "葵花宝典":
            return item
def find02():
    for item in list_skill:
        if item.id == 101:
            return item
def find03():
    for item in list_skill:
        if item.duration > 0:
            return item
"""
def condition04(item):
    return item.name == "葵花宝典"
def condition05(item):
    return item.id == 101
def condition06(item):
    return item.duration > 0
"""
def find(function_condition):
    for item in list_skill:
        # if item.duration > 0:
        # if condition03(item):
        if function_condition(item):
            return item
result = find(condition04)
print(result)
"""
print("=======================================")
result = ListHelper.find_single(list_skill,condition05)
print(result)

# 使用lambda实现
# 案例：查找名称是"葵花宝典"的技能
# 案例：查找编号是101的技能
# 案例：查找持续时间大于0的技能
result = ListHelper.find_single(list_skill,lambda  item:item.name=="葵花宝典")
print(result)
result = ListHelper.find_single(list_skill,lambda  item:item.id==101)
print(result)
result = ListHelper.find_single(list_skill,lambda  item:item.duration > 0)
print(result)

# 需求1:计算技能列表中技能名称大于4个字的技能数量
# 需求2:计算及鞥列表中技能持续时间小于等于5的技能数量
# 实现每个需求/封装变化/定义不变的函数(继承/多态)
# 将不变的函数提取到list_helper.py中
"""
def get_count01():
    count_value = 0
    for item in list_skill:
        if len(item.name) > 4:
            count_value += 1
    return count_value
def get_count02():
    count_value = 0
    for item in list_skill:
        if item.duration <= 5:
            count_value += 1
    return count_value
def get_count(function_duration):
    count_value = 0
    for item in list_skill:
        # if item.duration <= 5:
        if function_duration(item):
            count_value += 1
    return count_value
"""
print("#######################################")
result = ListHelper.get_count(list_skill,lambda item:len(item.name) > 4)
print(result)
result = ListHelper.get_count(list_skill,lambda item:item.duration <= 5)
print(result)