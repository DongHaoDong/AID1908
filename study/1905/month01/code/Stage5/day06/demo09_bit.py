"""
demo09_bit.py  位运算
"""
import numpy as np
a = np.array([-9,-5,2,1,-9])
b = np.array([-2,6,-2,3,-4])
print(a^b)
print(np.bitwise_xor(a,b))
c = a ^ b
print(np.where(c<0)[0])