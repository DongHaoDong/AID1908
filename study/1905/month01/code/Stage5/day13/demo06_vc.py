"""
demo06_vc.py   小汽车分类   验证曲线
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

# 读取文本数据，对每一列进行标签编码
# 整理样本空间，输入集与输出集
data = []
with open('../ml_data/car.txt','r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data)
print(data.shape)
train_x,train_y = [],[]
encoders = [] # 存储所有的标签编码器以后使用
for index,row in enumerate(data.T):
    encoder = sp.LabelEncoder()
    if index < (len(data.T)-1): # 添加到输入集
        train_x.append(encoder.fit_transform(row))
    else:   # 添加到输出集
        train_y=encoder.fit_transform(row)
    encoders.append(encoder)
train_x = np.array(train_x).T
train_y = np.array(train_y)
print(train_x.shape,train_y.shape)
print(train_x[0],train_y[0])

# # 训练随机森林分类器模型
# model = se.RandomForestClassifier(max_depth=9,n_estimators=150,random_state=7)
# # 验证曲线选择最优的n_estimators超参数
# train_scores,test_scores=ms.validation_curve(model,train_x,train_y,'max_depth',np.arange(1,11,1),cv=5)
# print(test_scores.mean(axis=1))
# # 绘制验证曲线结果
# mp.grid(linestyle=":")
# mp.plot(np.arange(100,200,10),test_scores.mean(axis=1),'o-',color='dodgerblue',label='validation curve')
# mp.legend()
# mp.show()




# 训练随机森林分类器模型
model = se.RandomForestClassifier(max_depth=9,n_estimators=150,random_state=7)
# 验证曲线选择最优的n_estimators超参数
train_scores,test_scores=ms.validation_curve(model,train_x,train_y,'n_estimators',np.arange(100,200,10),cv=5)
print(test_scores.mean(axis=1))

# 绘制验证曲线结果
mp.grid(linestyle=":")
mp.plot(np.arange(100,200,10),test_scores.mean(axis=1),'o-',color='dodgerblue',label='validation curve')
mp.legend()
mp.show()

model.fit(train_x,train_y)
# 自定义测试数据，用已训练好的模型进行测试
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]
data = np.array(data)
test_x,test_y = [],[]
for index,row in enumerate(data.T):
    encoder = encoders[index]
    if index < (len(data.T)-1): # 添加到输入集
        test_x.append(encoder.transform(row))
    else:   # 添加到输出集
        test_y=encoder.transform(row)
test_x = np.array(test_x).T
test_y = np.array(test_y)
# # 预测
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(test_y))
print(encoders[-1].inverse_transform(pred_test_y))
