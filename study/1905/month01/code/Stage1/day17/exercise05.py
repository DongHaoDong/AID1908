"""
# 1.使用生成器函数实现以上需求
# 2.体会函数式编程的封装
#   将三个函数变化点提取到另外三个函数中
#   将共性提取到另外一个函数中
# 3.体会函数式编程的继承与多态
#   使用变量隔离变化点，在共性函数中调用变量
# 4.测试(执行上述功能)
"""
list01 = [43,4,5,6,8,74]
# 需求：在列表中查找所有偶数
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item
# 需求：在列表中查找所有大于10的数
def find02():
    for item in list01:
        if item > 10:
            yield item
# 需求：在列表中查找所有范围在10 -- 50之间的数
def find03():
    for item in list01:
        if 10 < item < 50:
            yield item
# 封装
def comdotion01(item):
    return item % 2 == 0
def comdotion02(item):
    return item > 10
def comdotion03(item):
    return 10 < item < 50
# 继承
def find(function_condition):
    for item in list01:
        # 多态
        # 调用具体条件的抽象
        # 执行具体条件的函数
        if function_condition(item):
            yield item
for item in find(comdotion03):
    print(item)
# 方法参数，如果传递10/"张无忌"/True,叫传递数据
# 方法参数，如果函数1/函数2/函数3,叫逻辑
