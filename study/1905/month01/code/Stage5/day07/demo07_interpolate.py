"""
demo07_interpolate.py
"""
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 造一组散点
min_x = -50
max_x = 50
x = np.linspace(min_x,max_x,15)
y = np.sinc(x)
mp.grid(linestyle=":")
mp.scatter(x,y,s=60,color='dodgerblue',marker='o',label='Sample')
# 通过样本生成插值器函数
linear = si.interp1d(x,y,kind='linear')
linear_x = np.linspace(min_x,max_x,1000)
linear_y = linear(linear_x)
mp.plot(linear_x,linear_y,color='green',label='linear interpolation')
# 三次样条插值器
cubic = si.interp1d(x,y,kind='cubic')
cubic_x = np.linspace(min_x,max_x,1000)
cubic_y = cubic(cubic_x)
mp.plot(linear_x,cubic_y,color='orangered',label='cubic interpolation')
mp.legend()
mp.show()