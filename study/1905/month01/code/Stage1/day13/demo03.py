"""
    继承 -- 设计(1)

"""
# 需求：老张开车去东北
# 变化：       坐飞机     坐火车     骑车
# 违反了开闭原则
# 如果增加了火车需要增加火车类再修改人类中的go_to方法
class Person:
    def __init__(self,name):
        self.name = name
    def go_to(self,vehicle,str_position):
        if type(vehicle) == Car:
            vehicle.run(str_position)
        elif type(vehicle) == Airplane:
            vehicle.flay(str_position)
class Car:
    def run(self,str_position):
        print("汽车开到",str_position)
class Airplane:
    def flay(self,str_position):
        print("飞机飞到",str_position)
p01 = Person("老张")
c01 = Car()
p01.go_to(c01,"东北")
a01 = Airplane()
p01.go_to(a01,"东北")