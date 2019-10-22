"""
    多继承
    同名方法解析顺序：mro
"""
class A:
    def m01(self):
        print("A -- m01")
class B(A):
    def m01(self):
        print("B -- m01")
class C(A):
    def m01(self):
        print("c -- m01")
class D(B,C):
    def m02(self):
        self.m01()
d01 = D()
d01.m02()
# [D,B,C,A,object]
print(D.mro())