"""
    定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""
class MyRange:
    def __init__(self,stop_value):
        self.stop_value = stop_value
    def __iter__(self):
        return MyRangeIterator(self.stop_value)

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
for item in MyRange(5):
    print(item)