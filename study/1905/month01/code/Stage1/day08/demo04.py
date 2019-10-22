"""
    作用域
"""
# 全局变量
g01 = "OK"
# print(l01)
def fun01():
    # 局部变量：在函数内部定义的变量
    l01 = 100
# print(l01)
    print(l01)
    # 在函数内部可以读取全局变量
    # print(g01)
    # 创建了一个局部变量g01,而不是修改全局变量
    # g01 = "NO"

    # 定义全局变量g01
    global g01
    # 此时修改的是全局变量
    g01 = "NO"
    print(g01)

    # 定义全局变量g02
    global g02
    g02 = 250


fun01()
print(g01)
print(g02)