"""
协程行为
"""
from greenlet import greenlet
def fun01():
    print("执行fun01")
    gr2.switch()
    print("结束fun01")
    gr2.switch()
def fun02():
    print("执行fun02")
    gr1.switch()
    print("结束fun02")

# 将函数变成携程函数
gr1 = greenlet(fun01)
gr2 = greenlet(fun02)
gr1.switch()   # 选择执行哪个协程