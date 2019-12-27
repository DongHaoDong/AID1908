"""
demo05_ohe.py   独热编码
"""
import numpy as np
import sklearn.preprocessing as sp
samples = np.array([[1,3,2],[7,5,4],[1,8,6],[7,3,9]])
# 独热编码  sparse:是否采用稀疏矩阵
ohe = sp.OneHotEncoder(sparse=False,dtype='int32')
result = ohe.fit_transform(samples)
print(result)