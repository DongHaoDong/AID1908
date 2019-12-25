"""
demo11_eig.py  特征值和特征向量
"""
import numpy as np

A = np.mat('1 4 6 8; 4 9 1 2; 5 7 9 1; 4 2 8 3')
print(A)
# 提取特征值
eigvals,eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)

# 求圆方阵
eigvals[2:] = 0 # 抹掉部分特征值
A2 = eigvecs * np.diag(eigvals) * eigvecs.I
print(A2)