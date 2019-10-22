"""
    复习
        View    Controller  Model
        界面     业务逻辑    数据
        变化     变化       载体
"""
class XXController:
    def add_xx(self, a):
        print("Controller添加了数据", a)
class XXView:
    def __init__(self):
        self.controller = XXController()
    def input_xx(self):
        """
        需求：调用XXController类中的实例方法add_xx
        :return:
        """
        self.controller.add_xx(100)

view = XXView()
view.input_xx()

# 时序图