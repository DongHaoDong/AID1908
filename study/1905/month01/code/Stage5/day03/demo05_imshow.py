"""
demo05_imshow.py imshow图形化显示矩阵
"""
import numpy as np
import matplotlib.pyplot as mp
n = 1000
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# print(x, '-> x')
# print(y, '-> y')
z = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
mp.imshow(z,cmap='jet',origin='lower')
mp.colorbar()
mp.show()