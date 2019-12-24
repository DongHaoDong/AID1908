"""
demo09_attrs.py 属性测试
"""
import numpy as np
a = np.array([[1+1j,2+4j,3+7j],[4+2j,5+5j,6+8j],[7+3j,8+6j,9+9j]])
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.size)
print(a.nbytes)
print(a.real)
print(a.imag)
print(a.T)
print([x for x in a.flat])