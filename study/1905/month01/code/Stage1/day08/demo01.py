"""
    函数返回值   语法
"""
# 参数：调用者传递给定义着的信息
# 返回值：定义着传递给调用者的结果


def fun01(a):
    print("fun01执行了")
    # 作用：1.返回结果 2.退出方法
    return 20
    print("fun01又执行了")


# F8    逐过程     （调试时跳过方法）
# F7    逐语句     （调试时进入方法）
result = fun01(10)
print(result)


# 无返回值函数
def fun02(a):
    print("fun02执行了")
    # return None


re = fun02(10)
print(re)
