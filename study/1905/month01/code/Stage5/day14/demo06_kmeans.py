"""
demo06_kmeans.py kmean算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt',delimiter=',')
model = sc.KMeans(n_clusters=4)
model.fit(x)
pred_y = model.labels_
centers = model.cluster_centers_
print(centers)
# 绘制分类边界线
l,r = x[:,0].min()-1,x[:,0].max()+1
b,t = x[:,1].min()-1,x[:,1].max()+1
# 把可视区间划分为500*500
n = 500
grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
# 模拟使用模型，得到点阵中每个坐标的类别
mesh_x = np.column_stack((grid_x.ravel(),grid_y.ravel()))
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)
# pred_y = model.predict(x)
# 绘制这些点
mp.figure('K-Means Cluster', facecolor='lightgray')
mp.title('K-Means Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=pred_y,cmap='jet', s=80)
mp.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=1000, linewidth=4)
mp.show()