"""
    作业:调用fun07
"""

# |位置| |星号元组| |命名关键字| |双星字典|


def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args, end=" ")
    print(c)
    print(d)
    print(kwargs, end=" ")


fun07(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9)
print()

# 位置实参无限 + 关键字实参无限


def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


fun01()
fun01(1, 2, 3, a=4, c=5)
