"""
demo02_ndarray.py 测试ndarray
"""
import numpy as np
# 1
a = np.array([1,2,3,4,5,6])
print(a)
# 2
b = np.arange(1,10)
print(b)
# 3
c = np.zeros(10,dtype='int32')
print(c,c.dtype)
# 4
d = np.ones((2,3),dtype='float32')
print(d,d.shape,d.dtype)
# 5个1/5
print(np.ones(5) / 5)
# 扩展 np.zeros_like()    np.ones_like()
print(np.zeros_like(d))
print(np.ones_like(d))