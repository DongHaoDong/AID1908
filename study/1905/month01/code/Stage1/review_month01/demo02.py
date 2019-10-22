"""
    可变和不可变类型的传参
"""
def fun01(a):
    # 修改局部变量,对外部没有影响
    a = 1
g01 = 100
g02 = [1,2,3]
fun01(g02)
print(g02)

def fun02(a):
    # 通过变量，修改指向的对象，对外部有影响
    a[0] = "改了"
g03 = [1,2,3]
fun02(g03)
print(g03)

class MyClass01:
    pass
def fun03(p):
    # 通过变量，修改指向的对象，对外部有影响
    p.a = "改了"

c01 = MyClass01()
c01.a = 1
fun03(c01)
print(c01.a)