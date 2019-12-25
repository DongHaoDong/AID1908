"""
demo03_vectorize.py  函数矢量化
"""
import numpy as np
import math as m

def foo(x,y):
    return m.sqrt(x**2 + y**2)

x,y=3,4
print(foo(x,y))
x,y = np.array([3,4,5]),np.array([4,5,6])
# 矢量化foo函数 vectorize返回矢量化函数
foo_vec=np.vectorize(foo)
print(foo_vec(x,y))
print(np.vectorize(foo)(x,y).dtype)

# frompyfunc
foo_func = np.frompyfunc(foo,2,1)
print(foo_func(x,y).dtype)