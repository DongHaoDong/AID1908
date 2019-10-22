"""
    类    与    对象
        类：抽象的概念      类别
            人
            数据(变量)成员：身高/体重
            行为(函数/方法)成员：吃饭/睡觉
        对象：具体的事物    个体
            人
            dhd
            数据成员：183/60
            行为成员：吃饭/睡觉
            kk
            数据成员：175/80
            行为成员：吃饭/睡觉
"""


# 类
class Wife:
    # 数据成员
    def __init__(self, name, sex):
        # self是调用当前方法的对象地址
        self.name = name
        self.sex = sex
    # 行为成员
    def play(self):
        """
            一起玩耍
        """
        print("{}玩耍".format(self.name))

# 创建对象,实际在调用__init__方法
w01 = Wife("dream","女") # 自动将对象地址传入方法
# 调用对象的方法
w01.play()  # 自动将对象地址传入方法
