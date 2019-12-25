"""
demo07_add.py
"""
import numpy as np

a = np.arange(1,10)
print(a)
print(np.add(a,a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(a.prod())
print(a.cumprod())
print(np.add.outer([10,20,30],a))
print(np.outer([10,20,30],a))