"""
demo08_semilogy.py  刻度网格线
"""
import numpy as np

import matplotlib.pyplot as mp

mp.figure('Grid Line',facecolor='lightgray')
ax = mp.gca()
# 修改刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
ax.grid(which='major',axis='both',
        color='orangered',linewidth=0.75)
ax.grid(which='minor',axis='both',
        color='orangered',linewidth=0.25)
# 绘制曲线
y = [1,10,100,1000,100,10,1]
mp.semilogy(y,'o-',color='dodgerblue')
mp.show()
