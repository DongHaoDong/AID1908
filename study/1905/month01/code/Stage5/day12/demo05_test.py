"""
demo05_test.py
"""
import numpy as np
grid_x,grid_y = np.meshgrid(np.linspace(1,5,5),np.linspace(1,6,6))
print(grid_x)
print(grid_y)
import matplotlib.pyplot as mp
x = np.linspace(-40,40,5000)
y = 1/(1+np.exp(-x))
mp.plot(x,y)
mp.grid(linestyle=":")
mp.show()