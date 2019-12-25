"""
demo02_sign.py 数组简单处理
"""
import numpy as np

ary=np.array([60,40,-20,0,-8,15])
sign_ary = np.sign(ary)
print(sign_ary)
p_ary = np.piecewise(ary,[ary<0,ary==0,ary>0],[-1,0,1])
print(p_ary)