"""
    参照day10/exercise02.py
    完成练习
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
# 练习1:获取攻击比例大于6的所有技能
# 要求使用生成器函数/生成器表达式完成
def find01():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item
for item in find01():
    print(item)
for item in (item for item in list_skill if item.atk_ratio > 6):
    print(item)
print("=======================================================================")
# 练习2：获取持续时间在4--11之间的所有技能
def find02():
    for item in list_skill:
        if 4 <= item.duration <= 11:
            yield item
for item in find02():
    print(item)
for item in (item for item in list_skill if 4 <= item.duration <= 11):
    print(item)
print("===============================================================================")
# 练习3：获取技能编号是102的技能
def find03():
    for item in list_skill:
        if item.id == 102:
            return item
result = find03()
print(result)
for item in (item for item in list_skill if item.id == 102):
    print(item)
print("================================================================")
# 练习4：获取技能名称大于4个字并且持续时间小于6的所有技能
def find04():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item
for item in find04():
    print(item)
# 不建议使用生成器表达式
# for item in (item for item in list_skill if len(item.name) > 4 and item.duration < 6):
#     print(item)
