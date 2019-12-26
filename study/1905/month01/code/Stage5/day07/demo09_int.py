"""
demo09_int.py 定积分
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc

def f(x):
    return 2 * x ** 2 + 3 * x + 4

a,b=-5,5
x = np.linspace(a,b,1000)
y = f(x)
# 使用微元法求定积分
n = 50
px = np.linspace(a,b,n+1)
py = f(px)
# 遍历n个梯形，求每个梯形面积
area = 0
for i in range(n):
    area += (py[i+1]+py[i])*(px[i+1]-px[i]) / 2
print(area)
for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [px[i], 0], [px[i], py[i]],
        [px[i + 1], py[i + 1]], [px[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))
# 使用scipy求定积分
import scipy.integrate as si
r = si.quad(f,a,b)
print(r)
mp.grid(linestyle=":")
mp.plot(x,y,color='dodgerblue',linewidth=5)
mp.show()