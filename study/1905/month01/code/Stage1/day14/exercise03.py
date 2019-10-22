"""
    将day11/day10_exercise/exercise01.py中的
    Vector2和DoubleListHelper定义到double_list_helper模块中
    在exercise03.py中模块中 ，实现
        (1)在二维列表中，获取13位置，向左，3个元素
        (2)在二维列表中，获取22位置，向上，2个元素
        (3)在二维列表中，获取03位置，向下，2个元素
    要求使用三种导入方式
    观察那种方式方便
"""
list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]
# 方式一
# import double_list_helper as helper
# result = helper.DoubleListHelper.get_elements(list01,helper.Vector2(1,3),helper.Vector2.left())

# 方式二
# from double_list_helper import  DoubleListHelper
# from double_list_helper import Vector2
# result = DoubleListHelper.get_elements(list01,Vector2(1,3),Vector2.left())

# 方式三
from double_list_helper import *
result = DoubleListHelper.get_elements(list01,Vector2(1,3),Vector2.left())

