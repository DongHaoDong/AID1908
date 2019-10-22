"""
    迭代器 --> yield
"""
class MyRange:
    def __init__(self,stop_value):
        self.stop_value = stop_value
    def __iter__(self):
        # return MyRangeIterator(self.stop_value)
        # 0 --> self.stop_value
        # yield作用：将下列代码改为迭代器模式的代码
        # 生成迭代器代码的大致规则
        # 1.将yield以前的依据定义在next方法中
        # 2.将yield后面的数据作为next方法的返回值
        number = 0
        while number < self.stop_value:
            yield number
            number += 1
        # print("准备数据")
        # yield 0
        # print("准备数据")
        # yield 1
        # print("准备数据")
        # yield 2
"""
class MyRangeIterator:
    def __init__(self,end_value):
        self.__end_value = end_value
        self.__number = 0
    def __next__(self):
        if self.__number == self.__end_value:
            raise StopIteration
        temp = self.__number
        self.__number += 1
        return temp
"""
# for item in MyRange(10):
#     print(item)
my01 = MyRange(10)
iterator = my01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break