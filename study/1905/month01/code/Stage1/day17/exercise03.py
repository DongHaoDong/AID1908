"""
    1、获取列表中所有字符串
    2.获取列表中所有小数
    要求：分别使用生成器函数/生成器表达式/列表推导式完成
"""
list01 = [3,"54",True,456,"69",7.6,False,3.5]
def find01():
    for item in list01:
        if type(item) == str:
            yield item
result = find01()
for item in result:
    print(item)
result = (item for item in list01 if type(item) == str)
for item in result:
    print(item)
result = [item for item in list01 if type(item) == str]
for item in result:
    print(item)
# 练习2：
def find02():
    for item in list01:
        if type(item) == float:
            yield item
for item in find02():
    print(item)
for item in (item for item in list01 if type(item) == float):
    print(item)
for item in [item for item in list01 if type(item) == float]:
    print(item)