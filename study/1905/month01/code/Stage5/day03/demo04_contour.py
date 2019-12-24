"""
demo04_contour.py 等高线图
"""
import numpy as np
import matplotlib.pyplot as mp
n = 1000
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# print(x, '-> x')
# print(y, '-> y')
z = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
# 上述代码得到二维数组x,y直接组成点矩阵
# z为通过每个坐标的x与y计算而得的高度值
# (模拟采集的海拔高度)

# 画图
mp.figure('Contour',facecolor='lightgray')
mp.title('Contour',fontsize=16)
mp.grid(linestyle=":")
cntr = mp.contour(x,y,z,8,colors='black',linewidths=0.5)
# 设置等高线上的g高度标签文本
mp.clabel(cntr,fmt='%.2f',inline_spacing=2,fontsize=10)
mp.contourf(x,y,z,8,cmap='jet')
mp.show()


