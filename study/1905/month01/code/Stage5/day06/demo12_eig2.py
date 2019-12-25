"""
demo12_eig.py   读取图片
"""
import scipy.misc as sm
import numpy as np
import matplotlib.pyplot as mp

original = sm.imread('../da_data/lily.jpg',True)
print(original.shape)
# 提取特征值
original = np.mat(original)
eigvals,eigvecs = np.linalg.eig(original)
eigvals[50:]=0
dst=eigvecs*np.diag(eigvals) * eigvecs.I
mp.subplot(121)
mp.imshow(original,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(122)
mp.imshow(dst.real,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()