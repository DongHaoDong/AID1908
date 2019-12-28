"""
demo04_simple.py
"""
import numpy as np
import matplotlib.pyplot as mp
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# 绘制分类边界线
l,r = x[:,0].min()-1,x[:,0].max()+1
b,t = x[:,].min()-1,x[:,1].max()+1
# 把可视区间划分为500*500
n = 500
grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
# 模拟使用模型，得到点阵中每个坐标的类别
grid_z = np.piecewise(grid_x,[grid_x>grid_y,grid_x<grid_y],[0,1])
# 画图
mp.figure('Simple Classification',facecolor='lightgray')
mp.title('Simple Classification',fontsize=16)
mp.scatter(x[:,0],x[:,1],c=y,cmap='jet',label='Sample Points',s=70,zorder=3)
# 调用mp.pcolormesh()绘制分类边界线
# 根据参数，把可视区间拆分成坐标网格，由于每个网格都有相应的类别，可以使用cmap为每个网格填充颜色
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.legend()
mp.show()