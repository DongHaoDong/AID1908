"""
demo04_event.py 事件预测
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm


class DigitEncoder():
    """
    数字编码器,数字与字符串之间互转
    """
    def fit_transform(self,y):
        return y.astype(int)

    def transform(self,y):
        return y.astype(int)

    def inverse_transform(self,y):
        return y.astype(str)

# 读取数据 整理数据集
data = []
with open('../ml_data/events.txt','r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data)
# 删掉第一列，整理输入与输出集
data = np.delete(data,1,axis=1)
# 针对每一列做编码，
x,y,encoders = [],[],[]
for col in range(data.shape[1]):
    col_vals = data[:,col]
    if col_vals[0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    # 对当前列进行编码
    col_encoded = encoder.fit_transform(col_vals)
    if col < data.shape[1]-1:
        x.append(col_encoded)
    else:
        y = col_encoded
    encoders.append(encoder)
x = np.array(x).T
y = np.array(y).T
train_x,test_x,train_y,test_y=ms.train_test_split(x,y,test_size=0.25,random_state=7)
# 选择模型，训练模型
# model = svm.SVC(kernel='rbf',class_weight='balanced')
model = svm.SVC(kernel='rbf',degree=3,class_weight='balanced')
# import sklearn.naive_bayes as nb
# model = nb.GaussianNB()
model.fit(train_x,train_y)
# 预测
pred_test_y=model.predict(test_x)
import sklearn.metrics as sm
print(sm.classification_report(test_y,pred_test_y))
# 针对真实的业务场景进行预测
data = [['Tuesday','13:30:00','21','23']]
x = []
data = np.array(data)
for col in range(data.shape[1]):
    col_vals = data[:,col]
    encoder = encoders[col]
    # 对当前列进行编码
    col_encoded = encoder.transform(col_vals)
    x.append(col_encoded)
x = np.array(x).T
y = np.array(y)
print(x)
pred_y = model.predict(x)
print(pred_y,encoders[-1].inverse_transform(pred_y))