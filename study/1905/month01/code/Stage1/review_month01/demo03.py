"""
    参数
"""
# 位置形参/默认/关键字
def fun01(a,b,c=0,*,d):
    pass
fun01(1,2,d=3)
# 位置实参无限    [合并实参]
def fun02(*args):
    print(args)
fun02(2,3,4,5,6,9,8,7)
# 关键字实参无限制  [合并实参]
def fun03(**kwargs):
    print(kwargs)
fun03(a=1,b=2)

def fun04(a,b,c):
    pass
list01 = [1,2,3]
fun04(*list01)  # [拆分实参]

def fun05(a,b,c):
    pass
dict01 = {"a":1,"b":2,"c":3}
fun05(**dict01) # [拆分实参]