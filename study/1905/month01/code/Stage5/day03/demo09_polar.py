"""
demo09_polar.py
"""
import numpy as np
import matplotlib.pyplot as mp
mp.figure('Polar',facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar',fontsize=20)
mp.xlabel(r'$\theta$',fontsize=14)
mp.ylabel(r'$\rho$',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 准备数据
t = np.linspace(0,4*np.pi,1000)
r = 0.8 * t
mp.plot(t,r)
mp.show()
mp.show()