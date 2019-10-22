"""
    定义父类
        车(数据:速度，品牌)
    定义子类
        电动车(数据：电池容量，充电功率)
    创建两个对象，画出内存图
"""
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
class Electrocar(Car):
    def __init__(self,brand,speed,battery_capacity,charging_power):
        super().__init__(brand,speed)
        self.battery_battery = battery_capacity
        self.charging_power = charging_power
c01 = Car("奔驰",230)
print(c01.brand)
e01 = Electrocar("雅迪",120,15000,220)
print(e01.brand)
print(e01.charging_power)



