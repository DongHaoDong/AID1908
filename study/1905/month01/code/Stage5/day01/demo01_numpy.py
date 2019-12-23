"""
demo01_numpy.py 测试numpy
"""
import numpy as np

ary = np.array([1,2,3,4,5,6])
print(ary,type(ary))
print(ary.shape)  # 维度
ary.shape = (2,3)  # 维度改为2行3列
print(ary,ary.shape)
ary.shape = (6,)
# 数组的运算
print(ary)
print(ary * 3)
print(ary > 3)
print(ary + ary)