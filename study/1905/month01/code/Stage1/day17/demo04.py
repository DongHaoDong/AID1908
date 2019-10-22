"""
    lambda 匿名函数
        语法：lambda 参数列表:函数体
"""
from common.list_helper import *
list01 = [43,4,5,6,8,74]

# def comdotion01(item):
#     return item % 2 == 0
# def comdotion02(item):
#     return item > 10
# def comdotion03(item):
#     return 10 < item < 50

# for item in ListHelper.find_all(list01,comdotion02):
#     print(item)

for item in ListHelper.find_all(list01,lambda item:item % 2 == 0):
    print(item)
# ------------------------------------------
# 无参数函数 --> lambda
def fun01():
    return 100
a = lambda :100
result = a()
print(result)
# 多个参数函数 --> lambda
def fun02(p1,p2):
    return p1 > p2
b = lambda p1,p2:p1>p2
result = b(1,2)
print(result)
# 无返回值函数 --> lambda
def fun03(p1):
    print("参数是{}".format(p1))
c = lambda p1:print("参数是{}".format(p1))
c(100)
# 方法体只能有一条语句，且不支持赋值语句
def fun04(p1):
    p1 = 2
# d = lambda p1:p1=2