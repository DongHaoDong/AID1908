"""
将迭代器版本的图形管理器变为yield版本的
"""
class Graphic:
    pass
class GraphicManager:
    def __init__(self):
        self.__graphics = []
    def add_graphic(self,graphic):
            self.__graphics.append(graphic)
    def __iter__(self):
        # 程序执行过程：
        # 1.调用当前方法不执行(内部创建迭代器对象)
        # 2.调用__next__方法才执行
        # 3.指定yield语句暂时离开
        # 4.再次调用__next__方法继续执行
        # 5.重复第3-4步骤，直至最后
        for item in self.__graphics:
            yield item


manager = GraphicManager()
manager.add_graphic(Graphic)
manager.add_graphic(Graphic)
manager.add_graphic(Graphic)
# for item in manager:
#     print(item)
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
