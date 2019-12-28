"""
demo08_nb.py        朴素贝叶斯
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/multiple1.txt',delimiter=',')
x = data[:,:2].astype('f8')
y = data[:,-1].astype('f8')
print(x.shape,y.shape)
# 构建高斯朴素贝叶斯模型
model = nb.GaussianNB()
model.fit(x,y)
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

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()