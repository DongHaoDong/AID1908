"""
demo07_lossfunction.py  损失函数
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
xs = np.array([0.5,0.6,0.8,1.1,1.4])
ys = np.array([5.0,5.5,6.0,6.8,7.0])
n = 500
w0_grid,w1_grid = np.meshgrid(np.linspace(-3,10,n),np.linspace(-3,10,n))
loss=0
for x,y in zip(xs,ys):
    loss += (w0_grid+w1_grid*x-y)**2/2

# 画图
mp.figure('Loss Function',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0')
ax3d.set_ylabel('w1')
ax3d.set_zlabel('loss')
ax3d.plot_surface(w0_grid,w1_grid,loss,cstride=30,rstride=30,cmap='jet')
mp.tight_layout()
mp.show()