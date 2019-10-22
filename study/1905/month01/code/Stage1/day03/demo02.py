"""
    身份运算符
"""
a = 800
b = 1000
# id函数，可以获取变量存储的对象地址
print(id(a))
print(id(b))
# False
print(a is b)   # is的本质就是通过id函数进行判断的
# True
c = a
print(id(a))
print(id(c))
print(a is c)
# True
d = 1000
print(b is d)

