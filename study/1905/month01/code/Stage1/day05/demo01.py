"""
    列表
"""
# 1.创建列表
# 空列表
list01 = []
list01 = list()
# 默认值的列表
list02 = ["悟空", 100, True]
list02 = list("我是齐天大圣")
# 2.获取元素
# 索引
print(list02[2])
# 切片
print(list02[-4:])
# 3.添加元素
# 在末尾追加 append()
list02.append("八戒")
print(list02)
# 插入元素(在指定位置添加)   insert()
list02.insert(1, True)
print(list02)
# 4.删除元素
# 根据元素删除
list02.remove("是")
print(list02)
# 根据位置删除
del list02[0]
print(list02)
# 5.定义元素,目的:可以增删改查元素
# 切片
del list02[1:3]
print(list02)
list02[1:3] = ['天', '蓬']
# print(list02)
# list02[1:3] = []
# print(list02)
# 遍历列表
# 获取列表中的所有元素
for item in list02:
    print(item)
# 倒序获取列表中所有元素
# 不建议
# list02[::-1] 通过切片拿元素会重新创建新列表
# for item in list02[::-1]:
#     print(item)
# 3 2 1 0
for index in range(len(list02)-1, -1, -1):
    print(list02[index])
# -1 -2 -3 -4
for index in range(-1, -len(list02)-1, -1):
    print(list02[index])