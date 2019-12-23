"""
demo03_attr.py  属性测试
"""
import numpy as np

# 维度基础操作
a = np.arange(1,9)
print(a,a.shape)
a.shape = (2,4)
print(a,a.shape)
# 数据类型操作
print(a.dtype)
# a.dtype = 'float32'  # 错误的修改数据类型的方式
# print(a,a.dtype)
b = a.astype('float32')
print(b,b.dtype)
# size属性
print(b,' size:',b.size,' length:',len(b))
# 索引 下标 index操作
c = np.arange(1,19)
c.shape = (3,2,3)
print(c)
print(c[0])
print(c[0][1])
print(c[0][1][0])
print(c[0,1,0])
print(c.shape)
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k])
