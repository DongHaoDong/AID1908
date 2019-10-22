"""
函数式编程思想
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
# 封装(分而治之 变则疏之)
# 需求1:获取攻击比例大于6的所有技能
def find01():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item
# 需求2：获取持续时间在4--11之间的所有技能
def find02():
    for item in list_skill:
        if 4 <= item.duration <= 11:
            yield item
# 需求3：获取技能编号是102的技能
def find03():
    for item in list_skill:
        if item.id == 102:
            return item
# 需求4：获取技能名称大于4个字并且持续时间小于6的所有技能
def find04():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item
# 封装(分而治之 变则疏之)
# 将每个变化的条件单独定义在函数中
def condition01(item):
   return item.atk_ratio > 6
def condition02(item):
   return 4 <= item.duration <= 11
def condition03(item):
   return len(item.name) > 4 and item.duration < 6
# 继承，隔离变化
def find(function_condition):
    """
        通用的查找方法
    :param function_condition:查找条件，函数类型
        函数名(变量) --> 返回值bool类型
    :return:
    """
    for item in list_skill:
        # 多态:调用父(变量)，执行子(具体函数)
        #      不同子类重写父类方法，执行逻辑不同

        # if item.atk_ratio > 6:
        # if condition01(item):
        if function_condition(item):
            yield item
for item in find(condition01):
    print(item)

for item in find(condition02):
    print(item)