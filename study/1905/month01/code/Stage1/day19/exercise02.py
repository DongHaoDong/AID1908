"""
    在不改变原有功能调用与定义情况下，为其增加新功能
    打印函数执行时间
"""
import time

def print_execute_time(func):
    def wrapper(*args,**kwargs):
        # 记录调用前的时间
        start_time = time.time()
        result = func(*args,**kwargs)
        # 记录调用后的时间
        execute_time = time.time() - start_time
        print("执行时间是:",execute_time)
        return result
    return wrapper
@print_execute_time
def fun01():
    time.sleep(2)
    print("fun01执行完毕了")
@print_execute_time
def fun02(a):
    time.sleep(2)
    print("fun02执行完毕了参数是:",a)
fun01()
fun02(100)