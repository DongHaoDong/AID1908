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
def condition01(item):
    return item.name == "葵花宝典"
def condition02(item):
    return item.id == 101
def condition03(item):
    return item.duration > 0
def find(function_condition):
    for item in list_skill:
        # if item.duration > 0:
        # if condition03(item):
        if function_condition(item):
            return item
result = find(condition03)
print(result)