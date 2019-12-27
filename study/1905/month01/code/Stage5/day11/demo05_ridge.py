"""
demo05_ridge.py 岭回归
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import pickle
import sklearn.metrics as sm

# 采集数据，读文本
x,y=np.loadtxt(
    '../ml_data/abnormal.txt',delimiter=',',unpack=True
)
# 整理输入集(二维)与输出集(一维)
x=x.reshape(-1,1) # 变维:n行1列
mp.figure('Ridge Regression',facecolor='lightgray')
mp.title('Ridge Regression',fontsize=18)
mp.grid(linestyle=":")
mp.scatter(x,y,s=70,color='dodgerblue',label='Sample Points')
# 普通线性回归
model = lm.LinearRegression()
model.fit(x,y)
pred_y = model.predict(x)
mp.plot(x,pred_y,color='orangered',label='LR')
print(sm.r2_score(y,pred_y))
# 岭回归
model = lm.Ridge(100,fit_intercept=True,max_iter=1000)
model.fit(x,y)
pred_y = model.predict(x)
print(sm.r2_score(y,pred_y))
mp.plot(x,pred_y,color='green',label='Ridge')
mp.legend()
mp.show()

