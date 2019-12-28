"""
demo03_gridsearch.py     网格搜索
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.model_selection as ms
data = np.loadtxt('../ml_data/multiple2.txt',delimiter=',')
x = data[:,:2].astype('f8')
y = data[:,-1].astype('f8')
print(x.shape,y.shape)

# 拆分测试集与训练集
train_x,test_x,train_y,test_y=ms.train_test_split(x,y,test_size=0.25,random_state=7)

# 构建高斯朴素贝叶斯模型
model = svm.SVC(probability=True)
# 网格搜索确定最优超参数
params = [
    {'kernel':['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]},
    {'kernel':['rbf'], 'C':[1,10,100,1000],
     'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(model,params,cv=5)
model.fit(train_x,train_y)
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
# 输出交叉验证结果
for p,s in zip(model.cv_results_['params'],model.cv_results_['mean_test_score']):
    print(p,s)
import sklearn.metrics as sm
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y,pred_test_y))
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

mp.figure('SVM Classification', facecolor='lightgray')
mp.title('SVM Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=80)
# 新增一些点，输出置信概率
# 整理测试样本
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_brob_y = model.predict(prob_x)
mp.scatter(prob_x[:, 0], prob_x[:, 1],marker='D', c=pred_brob_y, cmap='jet_r', s=80)
probs = model.predict_proba(prob_x)
print(probs)
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})
mp.show()