"""
demo02_bar.py
"""
import numpy as np
import matplotlib.pyplot as mp

apples = np.array([82,34,46,58,46,58,35,41,46,13,42,44])
oranges = np.array([69,76,23,84,61,25,21,34,82,69,12,34])

# 绘制柱状图
mp.figure('Bar',facecolor='lightgray')
mp.title('Bar Chart',fontsize=18)
mp.grid(linestyle=':')
x = np.arange(apples.size)
y = np.arange(oranges.size)
mp.bar(x-0.2,apples,0.4,color='limegreen',label='Apple',align='center')
mp.bar(y+0.2,oranges,0.4,color='orangered',label='Oranges',align='center')
# 设置刻度
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
mp.legend()
mp.show()