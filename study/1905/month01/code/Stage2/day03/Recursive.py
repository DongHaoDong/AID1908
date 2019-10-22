"""
利用递归求一个数的阶乘
"""
def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num-1)
print(recursion(5))