"""
    员工管理器记录多个员工
    迭代员工管理器对象
"""
class Employee:
    pass
class EmployeeManager:
    def __init__(self):
        self.__employees = []
    def add_employee(self,employees):
        self.__employees.append(employees)
    def __iter__(self):
        return EmployeeIterator(self.__employees)
class EmployeeIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0
    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp
manager = EmployeeManager()
manager.add_employee(Employee)
manager.add_employee(Employee)
manager.add_employee(Employee)

for item in manager:
    print(item)
# 多态
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break