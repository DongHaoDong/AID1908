"""
demo01_svd.py   奇异值分解
"""
import numpy as np

M = np.mat('4 -11 14; 8 7 -2')
print(M)
# svd奇异值分解
np.linalg.svd(M)
U,sv,V = np.linalg.svd(M,full_matrices=False)
# U与V是正交矩阵
print(U * U.T)
print(V * V.T)
print(U.shape,sv.shape,V.shape)
sv[1:] = 0
# 推导原矩阵
M2 = U * np.diag(sv) * V
print(M2)