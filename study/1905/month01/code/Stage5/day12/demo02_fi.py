"""
demo02_fi.py 特征重要性
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm
import matplotlib.pyplot as mp

boston = sd.load_boston()
print(boston.data.shape)    # 输入数据
print(boston.data[0])
print(boston.target.shape)  # 输出数据
print(boston.target[0])
print(boston.feature_names) # 输入数据的特征名
names = boston.feature_names
# 打乱原始数据集，拆分训练集与测试集
# random_state:随机种子
# 使用相同的随机种子多次打乱得到的结果是一致的
x,y=su.shuffle(boston.data,boston.target,random_state=7)
train_size = int(len(x)*0.8)
train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
# 构建决策树模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)
# 评估结果
r = sm.r2_score(test_y,pred_test_y)
print(r)
dt_fi = model.feature_importances_
print('DT FI:',dt_fi)

# 构建Addaboost模型
import sklearn.ensemble as se
model = se.AdaBoostRegressor(model,n_estimators=400,random_state=7)
model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)
r = sm.r2_score(test_y,pred_test_y)
print(r)
ada_fi = model.feature_importances_
print('AdaBoost FI:',ada_fi)

# 画图绘制特征重要性指标
mp.figure('Feature Importances',facecolor='lightgray')
mp.subplot(211)
mp.title('DT Feature Importances', fontsize=16)
mp.ylabel('Feature Importances',fontsize=14)
mp.grid(linestyle=":")
x = np.arange(dt_fi.size)
# 对fi进行排序，得到有序索引
sorted_indices = dt_fi.argsort()[::-1]
dt_fi = dt_fi[sorted_indices]
mp.bar(x,dt_fi,0.8,color='dodgerblue',label="DT Feature Importances")
# 控制x轴刻度
mp.xticks(x,names[sorted_indices])
mp.legend()
mp.tight_layout()
mp.subplot(212)
mp.title('AdaBoost Feature Importances', fontsize=16)
mp.ylabel('Feature Importances',fontsize=14)
mp.grid(linestyle=":")
x = np.arange(dt_fi.size)
# 对fi进行排序，得到有序索引
sorted_indices = ada_fi.argsort()[::-1]
ada_fi = ada_fi[sorted_indices]
mp.bar(x,ada_fi,0.8,color='orangered',label="AdaBoost Feature Importances")
# 控制x轴刻度
mp.xticks(x,names[sorted_indices])
mp.legend()
mp.tight_layout()
mp.show()

