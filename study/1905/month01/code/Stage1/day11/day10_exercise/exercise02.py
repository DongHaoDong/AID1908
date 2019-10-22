"""
定义敌人类
    --数据：姓名,血量,基础攻击类,防御力
    --行为：打印个人信息
    创建敌人列表(至少4个元素),并画出内存图
    查找姓名是"灭霸"的敌人对象
    查找所有死亡的敌人
    计算所有敌人的平均攻击力
    删除防御力小于10的攻击力
    将所有敌人攻击力增加50
"""
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
    def print_self_info(self):
        print(self.name,self.hp,self.atk,self.defense)
list01 = [
    Enemy("玄冥二老",86,120,58),
    Enemy("成昆",0,100,5),
    Enemy("谢逊",120,130,60),
    Enemy("灭霸",0,1309,690),
]
# 查找姓名是"灭霸"的敌人对象
def find01():
    for item in list01:
        if item.name == "灭霸":
            return item
e01 = find01()
# 如果没找到，返回值为None
# 所以可以判断不是空,再调用其实例方法
# if e01 != None:
if e01:
    e01.print_self_info()
else:
    print("没找到！")
# 查找所有死亡的敌人
def find02():
    list_result = []
    for item in list01:
        if item.hp == 0:
            list_result.append(item)
    return list_result
result = find02()
for item in result:
    item.print_self_info()
# 计算所有敌人的平均攻击力
def calculate():
    sum_atk = 0
    for item in list01:
        sum_atk += item.atk
    return sum_atk / len(list01)
print(calculate())
# 删除防御力小于10的攻击力
def delete01():
    for i in range(len(list01)-1,-1,-1):
        if list01[i].defense < 10:
            del list01[i]
delete01()
for item in list01:
    item.print_self_info()
# 将所有敌人攻击力增加50
def set01():
    for item in list01:
        item.atk += 50
set01()
for item in list01:
    item.print_self_info()
