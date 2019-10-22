"""
    运算符重载
"""
class Vector1:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return str(self.x)
    def __add__(self, other):
        return Vector1(self.x+other)
    def __radd__(self, other):
        return Vector1(self.x + other)
    def __iadd__(self, other):
        self.x += other
        return self
v01 = Vector1(10)
print(v01+2)
print(2+v01)

print(id(v01))
# 重写 __iadd__，实现在原对象基础上的变化
# 如果不重写 __iadd__，默认使用 __add__,一般产生新对象
v01 += 2
print(v01,id(v01))

# list01 = [1]
# print(id(list01))
# # 生成新对象
# re = list01 + [2]
# print(re)
# # 在原有基础上累加
# list01 += [2]
# print(list01,id(list01))
