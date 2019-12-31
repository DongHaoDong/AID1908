"""
demo02_dbscan.py    DBSCAN算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

x = np.loadtxt('../ml_data/perf.txt',delimiter=',')
# 优选半径参数
eps,scores,models = np.linspace(0.3,1.0,8),[],[]
for r in eps:
    model = sc.DBSCAN(eps=r,min_samples=5)
    model.fit(x)
    labels = model.labels_
    score = sm.silhouette_score(x,labels,sample_size=len(x),metric='euclidean')
    scores.append(score)
    models.append(model)
scores = np.array(scores)
models = np.array(models)
# 获最优得分index
best_index = scores.argmax()
best_model = models[best_index]
best_score = scores[best_index]
best_r = eps[best_index]
print(best_r,best_score,best_model)
# 绘制图像
mp.figure('DBSCAN Cluster', facecolor='lightgray')
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
labels = best_model.labels_
# 获取核心样本，孤立样本，外周样本
core_mask = np.zeros(len(x),dtype='bool')
core_mask[best_model.core_sample_indices_] = True
# 绘制核心样本
mp.scatter(x[core_mask][:,0],x[core_mask][:,1],c=labels[core_mask],cmap='jet',s=70)
offset_mask = labels == -1
# 绘制孤立样本
mp.scatter(x[offset_mask][:,0],x[offset_mask][:,1],marker='D',color='black',s=80,alpha=0.4)
# 绘制外周样本
p_mask = ~(core_mask | offset_mask)
mp.scatter(x[p_mask][:,0],x[p_mask][:,1],c=labels[p_mask],cmap='jet',marker='s',s=70,alpha=0.8)
mp.show()
