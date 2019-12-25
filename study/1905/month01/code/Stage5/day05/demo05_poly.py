"""
demo05_poly.py 测试多项式函数相关API
"""
import numpy as np
import matplotlib.pyplot as mp

P = [4,3,-1000,1]
x = np.linspace(-20,20,1000)
y = np.polyval(P,x)

# 求多项式函数的导函数
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P,xs)
mp.scatter(xs,ys,color='red',s=60)
mp.plot(x,y)
mp.show()
