"""
    生成器表达式
"""
list01 = [3,"54",True,456,"69",7.6,False,3.5]
# 生成器函数
def find01():
    for item in list01:
        if type(item) == int:
            yield item + 1
result = find01()
for item in result:
    print(item)
# 生成器表达式
# 此时没有计算，更没有结果
result = (item + 1 for item in list01 if type(item) == int)
# 一次循环，一次计算，一个结果
for item in result:
    print(item)
# 列表推导式
# 此时已经完成所有计算，得到所有结果
result = [item + 1 for item in list01 if type(item) == int]
# 只是获取所有结果
for item in result:
    print(item)
# 变量 = [item for item in 可迭代对象 if 条件]列表推导式
# 变量 = {k,v for k,v in 可迭代对象 if 条件}字典推导式
# 变量 = {item for item in 可迭代对象 if 条件}集合推导式
# 变量 = (item for item in 可迭代对象 if 条件)生成器表达式