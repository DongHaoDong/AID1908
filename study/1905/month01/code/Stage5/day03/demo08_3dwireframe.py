"""
demo08_3dwireframe.py 三维线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n = 1000
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# print(x, '-> x')
# print(y, '-> y')
z = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
# 上述代码得到二维数组x,y直接组成点矩阵
# z为通过每个坐标的x与y计算而得的高度值
# (模拟采集的海拔高度)

# 画图
mp.figure('3D wireframe',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.plot_wireframe(x,y,z,cstride=30,rstride=30,linewidth=1,color='dodgerblue')
mp.show()


