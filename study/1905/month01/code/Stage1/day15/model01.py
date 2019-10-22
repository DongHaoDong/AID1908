# 定义当前模块哪些成员可以被from 模块 import * 导入
__all__=["fun01","MyClass","_fun02"]
print("模块1")
def fun01():
    print("模块1的fun01")
# 只是在模块内部使用的成员，可以以单下划线开头
# 只限于from 模块 import * 有效
def _fun02():
    print("模块1的fun02")
class MyClass:
    @staticmethod
    def fun03():
        print("MyClass -- fun03")
print(__name__)