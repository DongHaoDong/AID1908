"""
demo06_3dscatter.py 三维散点图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n=300
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)
# 绘制三维点阵
mp.figure('3D scatter',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
d = x**2 + y**2 + z**2
ax3d.scatter(x,y,z,s=60,marker='o',c=d,cmap='jet')

mp.show()