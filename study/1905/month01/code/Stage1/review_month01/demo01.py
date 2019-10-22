"""
    容器
"""
# 字符串
str01 = "最后一节课"
# 列表-->预留空间
list01 = [4,5,5,8,9,6]
# 元组-->按需分配
tuple01 = (5,6,7,8)
# 字典
dict01 = {"键":"值"}
# 容器相互转换
# str --> list
list02 = list(str01)
print(list02)
# list --> str
str02 ="".join(list02)
print(str02)
# list --> tuple
tuple02 = tuple(list01)
print(tuple02)
# 容器名称(可迭代对象)

# 通用操作
# print(id(list01))
# list01 += ["a"]   # 在原有基础上累加
# print(list01)
# print(id(list01))

print(id(tuple01))
tuple01 += ("b",)   # 由于元祖不可变，所以创建新对象
print(tuple01)
print(id(tuple01))

if "键2" in dict01:
    print(dict01["键2"])
# 获取所有元素
for item in str01:
    print(item)
# 正向索引
# 0 1 2 3 4
for index in range(-len(str01),0):
    print(str01[index],end=" ")
# 反向索引
# -5 -4 -3 -2 -1
for index in range(len(str01)):
    print(str01[index],end=" ")

# 正向索引倒叙获取
# 4 3 2 1 0
# for index in range(len(list01)-1,-1,-1):
#     del list01[index]

# 反向索引正序获取
# -5 -4 -3 -2 -1
for index in range(-len(list01),0):
    del list01[index]
print(list01)
