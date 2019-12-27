"""
demo03_dump.py 模型的保存
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import pickle

# 采集数据，读文本
x,y=np.loadtxt(
    '../ml_data/single.txt',delimiter=',',unpack=True
)
# 整理输入集(二维)与输出集(一维)
x=x.reshape(-1,1) # 变维:n行1列
# 构建线性回归模型,训练模型
model = lm.LinearRegression()
# 针对训练数据，得到预测结果，画图
model.fit(x,y)
# 存储模型
with open('linear.pkl','wb') as f:
    pickle.dump(model,f)
    print('dump success!')


