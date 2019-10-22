"""
    函数参数
        形式参数
"""
# 1.缺省(默认)形参：如果实参不提供,可以使用默认值
def fun01(a = 0, b = 0, c = 0, d = 0):
    print(a)
    print(b)
    print(c)
    print(d)
# 关键字实参 + 缺省形参：调用者可以随意传递参数
fun01(b=2, c=3)
# 2.位置形参：
def fun02(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)
# 3.星号元组形参：*将所有实参合并为一个元组
# 作用：让实参个数无限
def fun03(*args):
    print(args)
fun03()
fun03(1)
fun03(1, "2")
# 4.关键字形参：在星号元组形参以后的位置形参
# 要求：要求实参必须使用关键字实参
def fun04(a, *args, b):
    print(a)
    print(args)
    print(b)
fun04(1,b=2)
fun04(1, 2, 3, 4, b=2)

def fun05(*, a, b):
    print(a)
    print(b)
fun05(a=1,b=2)

# 5.双星号字典形参：**目的是将实参合并为字典
#               实参可以传递数量无限的关键字实参
def fun06(**kwargs):
    print(kwargs)
fun06(a=1,b=2)
# 作业调用fun07
def fun07(a,b,*args,c,d,**kwargs):
    pass



