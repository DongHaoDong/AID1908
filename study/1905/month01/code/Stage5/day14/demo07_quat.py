"""
demo07_quat.py      图像量化
"""
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import sklearn.cluster as sc
import matplotlib.pyplot as mp
# 读取原始图像
original = sm.imread('../ml_data/lily.jpg',True)
print(original.shape)
mp.subplot(121)
mp.imshow(original,cmap='gray')
mp.axis('off')
mp.tight_layout()
# 基于KMean图像量化
model = sc.KMeans(n_clusters=4)
x = original.reshape(-1,1)
model.fit(x)
y = model.labels_
centers = model.cluster_centers_
print(y)
print(centers)
newimage = centers[y].reshape(original.shape)
mp.subplot(122)
mp.imshow(newimage,cmap='gray')
mp.axis('off')
mp.tight_layout()
mp.show()