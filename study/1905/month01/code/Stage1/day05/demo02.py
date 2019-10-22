"""
    列表内存图
"""
list01 = ["张无忌", "赵敏"]
list02 = list01
# 修改的是列表的第一个元素
list01[0] = "无忌"
print(list02[0])
list01 = ["张无忌", "赵敏"]
list02 = list01
# 修改的是变量list01
list01 = ["无忌"]
print(list02[0])

list01 = [800, 1000]
# 通过切片获取元素会创建新列表
list02 = list01[:]
list01[0] = 900
print(list02[0])
list01 = [500]
print(list02[0])

list01 = [800, [1000, 500]]
# 通过切片获取元素会创建新列表
list02 = list01
list01[1][0] = 900
print(list02[1][0])

list01 = [800, [1000, 500]]
# 浅拷贝
# list02 = list01[:]
list02 = list01.copy()
list01[1][0] = 900
print(list02[1][0])

import copy
list01 = [800, [1000, 500]]
# 深拷贝
list02 = copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])
