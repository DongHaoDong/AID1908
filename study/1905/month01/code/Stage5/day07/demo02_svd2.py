"""
demo12_svd2.py   奇异值分解 提取图片奇异值
"""
import scipy.misc as sm
import numpy as np
import matplotlib.pyplot as mp

original = sm.imread('../da_data/lily.jpg',True)
print(original.shape)
# 提取特征值
original = np.mat(original)
eigvals,eigvecs = np.linalg.eig(original)
# 抹掉一部分特征值，生成新图片
eigvals[50:]=0
dst=eigvecs*np.diag(eigvals) * eigvecs.I
# 奇异值分解
original = np.mat(original)
U,sv,V = np.linalg.svd(original)
sv[50:]
dst2 = U * np.diag(sv) * V
mp.subplot(221)
mp.imshow(original,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(222)
mp.imshow(dst.real,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.subplot(224)
mp.imshow(dst2.real,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()