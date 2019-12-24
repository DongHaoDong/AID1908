"""
demo08_stack.py 数组的组合与拆分
"""
import numpy as np
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
print(a, '--> a')
print(b, '--> b')
# 水平方向
c = np.hstack((a,b))
print(c, '--> c')
a,b = np.hsplit(c,2)
print(a, '--> a')
print(b, '--> b')
# 垂直方向
c = np.vstack((a,b))
print(c, '--> c')
a,b = np.vsplit(c,2)
print(a, '--> a')
print(b, '--> b')
# 深度方向
c = np.dstack((a,b))
print(c, '--> dc')
a,b = np.dsplit(c,2)
print(a, '--> da')
print(b, '--> db')
# 一维数组的组合方案
a = np.arange(1,9)
b = np.arange(9,17)
print(a)
print(b)
print(np.row_stack((a,b)))  # 形成两行
print(np.column_stack((a,b)))  # 形成两列
