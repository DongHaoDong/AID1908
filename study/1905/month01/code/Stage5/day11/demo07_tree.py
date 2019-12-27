"""
demo07_tree.py  决策树
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.utils as su

boston = sd.load_boston()
print(boston.data.shape)    # 输入数据
print(boston.data[0])
print(boston.target.shape)  # 输出数据
print(boston.target[0])
print(boston.feature_names) # 输入数据的特征名

# 打乱原始数据集，拆分训练集与测试集
# random_state:随机种子
# 使用相同的随机种子多次打乱得到的结果是一致的
x,y=su.shuffle(boston.data,boston.target,random_state=7)
train_size = int(len(x)*0.8)
train_x,test_x,train_y,test_y=x[:train_size],x[train_size:],y[:train_size],y[train_size:]
# 构建决策树模型
import sklearn.tree as st
import sklearn.metrics as sm
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)
# 评估结果
r = sm.r2_score(test_y,pred_test_y)
print(r)
print(sm.mean_absolute_error(test_y,pred_test_y))