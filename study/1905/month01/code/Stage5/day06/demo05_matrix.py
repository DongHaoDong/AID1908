"""
demo05_matrix.py 矩阵
"""
import numpy as np

ary = np.arange(1,10).reshape(3,3)
print(ary,ary.shape,type(ary))
# 第一种创建方式
m = np.matrix(ary,copy=True)
print(m,m.shape,type(m))
# 第二种创建方式
m2 = np.mat(ary)
print(m2)
# 第三种创建方式
m3 = np.mat('1 2 3; 4 5 6')
print(m3,m3.dtype)
# 乘法运算
print(ary * ary,'-> ary*ary')
print(m * m,'m*m')
# 矩阵求逆
m = np.mat('1 4 8; 4 9 2; 1 6 9')
print(m)
print(m.I)
print(m * m.I)
# 把逆矩阵的定义推广到非方阵，称为广义逆矩阵
m = m[:2,:]
print(m)
print(m.I)
print(m * m.I)

# 解方程
prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')
# 使用np提供的API解方程
x = np.linalg.lstsq(prices,totals)[0]
print(x)
x = np.linalg.solve(prices,totals)
print(x)
x = prices.I * totals
print(x)
# 输出斐波那契数列
n = 32
F = np.mat('1 1; 1 0')
for i in range(1,n):
    print((F**i)[0,0])
print(F**0)