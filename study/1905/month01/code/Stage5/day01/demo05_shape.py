"""
demo05_shape.py  维度处理
"""
import numpy as np

a = np.arange(1,10)
print(a)
# 视图变维
b = a.reshape(3,3)
print(a, '-> a')
a[0] = 999
print(b, '-> b')
print(b.ravel())  # 抻平数组
# 复制变维
c = b.flatten()
print(c, '-> c')
b[0][0] = 88
print(c, '-> c')
# 就地变维
c.shape = (3,3)
print(c, '-> c')
c.resize((9,))
print(c, '-> c')


