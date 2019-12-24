"""
demo01_plot.py 基本绘图
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([1,2,3,4,5,6])
y = np.array([12,39,36,25,13,41])
# 绘制水平线，垂直线
mp.hlines([10,20,30,40],[1,2,3,4],[2,3,4,5])
mp.vlines(4,10,35)
mp.plot(x,y)
mp.show()