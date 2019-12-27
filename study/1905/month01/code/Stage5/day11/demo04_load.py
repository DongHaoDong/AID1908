"""
demo04_load.py 模型加载
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
mp.figure('Linear Regression',facecolor='lightgray')
mp.title('Linear Regression',fontsize=18)
mp.grid(linestyle=":")
mp.scatter(x,y,s=70,color='dodgerblue',label='Sample Points')
# 模型从文件中加载而来
with open('linear.pkl','rb') as f:
    model = pickle.load(f)
pre_y=model.predict(x)
# 评估当前模型效果
import sklearn.metrics as sm
print(sm.mean_absolute_error(y,pre_y))
print(sm.mean_squared_error(y,pre_y))
print(sm.median_absolute_error(y,pre_y))
print(sm.r2_score(y,pre_y))
mp.plot(x,pre_y,color='orangered',label='Regression Line')
mp.legend()
mp.show()

