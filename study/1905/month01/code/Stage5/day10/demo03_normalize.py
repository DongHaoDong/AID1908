"""
demo03_normalize.py 归一化
"""
import numpy as np
import sklearn.preprocessing as sp

ary = np.array([[10,21,5],[2,4,1],[11,18,18]])
# 归一化
result = sp.normalize(ary,norm='l1')
print(result)
