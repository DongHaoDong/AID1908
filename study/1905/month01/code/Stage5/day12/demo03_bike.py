"""
demo03_bike.py      预测共享单车使用量
"""
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = []
with open('../ml_data/bike_day.csv','r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
# 整理输入与输出集
day_header = np.array(data[0][2:13])
x = np.array(data[1:])[:,2:13].astype('f8')
y = np.array(data[1:])[:,-1].astype('f8')
# 打乱数据集，拆分训练集和测试集
x,y=su.shuffle(x,y,random_state=7)
train_size = int(len(x)*0.9)
train_x,test_x,train_y,test_y = x[:train_size],x[train_size:],y[:train_size],y[train_size:]
# 训练随机森林模型
model = se.RandomForestRegressor(max_depth=10,n_estimators=1000,min_samples_split=2)
model.fit(train_x,train_y)
# 输出预测结果r2得分
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y,pred_test_y))
day_fi = model.feature_importances_
data = []
with open('../ml_data/bike_hour.csv','r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
# 整理输入与输出集
hour_header = np.array(data[0][2:14])
x = np.array(data[1:])[:,2:14].astype('f8')
y = np.array(data[1:])[:,-1].astype('f8')
# 打乱数据集，拆分训练集和测试集
x,y=su.shuffle(x,y,random_state=7)
train_size = int(len(x)*0.9)
train_x,test_x,train_y,test_y = x[:train_size],x[train_size:],y[:train_size],y[train_size:]
# 训练随机森林模型
model = se.RandomForestRegressor(max_depth=10,n_estimators=1000,min_samples_split=2)
model.fit(train_x,train_y)
# 输出预测结果r2得分
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y,pred_test_y))
hour_fi = model.feature_importances_
# 画图绘制特征重要性指标
mp.figure('Feature Importances',facecolor='lightgray')
mp.subplot(211)
mp.title('DAY Feature Importances', fontsize=16)
mp.ylabel('Feature Importances',fontsize=14)
mp.grid(linestyle=":")
x = np.arange(day_fi.size)
# 对fi进行排序，得到有序索引
sorted_indices = day_fi.argsort()[::-1]
day_fi = day_fi[sorted_indices]
mp.bar(x,day_fi,0.8,color='dodgerblue',label="DAY Feature Importances")
# 控制x轴刻度
mp.xticks(x,day_header[sorted_indices])
mp.legend()
mp.tight_layout()
mp.subplot(212)
mp.title('Hour Feature Importances', fontsize=16)
mp.ylabel('Feature Importances',fontsize=14)
mp.grid(linestyle=":")
x = np.arange(hour_fi.size)
# 对fi进行排序，得到有序索引
sorted_indices = hour_fi.argsort()[::-1]
hour_fi = hour_fi[sorted_indices]
mp.bar(x,hour_fi,0.8,color='orangered',label="Hour Feature Importances")
# 控制x轴刻度
mp.xticks(x,hour_header[sorted_indices])
mp.legend()
mp.tight_layout()
mp.show()



