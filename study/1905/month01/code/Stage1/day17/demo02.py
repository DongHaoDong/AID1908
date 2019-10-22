"""
    函数式编程
"""
def fun01():
    print("fun01执行了")
# 调用方法执行方法体
re = fun01()
print(re)
# 将函数赋值给变量
re2 = fun01
# 通过变量调用函数
re2()
def fun02():
    print("fun02执行了")
# 将函数作为函数的参数进行传递
# 将一个函数的代码注入到另外一个函数中
def fun03(func):
    print("fun03执行了")
    func()
fun03(fun01)
fun03(fun02)