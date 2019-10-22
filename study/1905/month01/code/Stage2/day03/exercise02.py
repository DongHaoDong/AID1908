"""
求一个数的阶乘
"""
def fun(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
print(fun(999999999))
