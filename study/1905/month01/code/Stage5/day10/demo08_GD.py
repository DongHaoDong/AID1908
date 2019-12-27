"""
demo08_GD.py    梯度下降实现线性回归
"""
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5,0.6,0.8,1.1,1.4])
train_y = np.array([5.0,5.5,6.0,6.8,7.0])

w0,w1 = 1,1
times = 1000
lrate = 0.01
for i in range(1,times+1):
    # 求损失函数关于w0与w1的偏导数，从而更新模型参数
    d0 = (w0+w1*train_x-train_y).sum()
    d1 = (train_x*(w0+w1*train_x-train_y)).sum()
    # 根据梯度下降公式,更新w0与w1
    w0 = w0 -lrate * d0
    w1 = w1 -lrate * d1
print('w0:',w0)
print('w1:',w1)
# 绘制回归线
linex = np.linspace(train_x.min(),train_y.max(),100)
liney = w1 * linex + w0
# 画图
mp.figure('Linear Regression',facecolor='lightgray')
mp.title('Linear Regression',fontsize=18)
mp.grid(linestyle=':')
mp.scatter(train_x,train_y,s=80,marker='o',color='dodgerblue',label='Samples')
mp.plot(linex,liney,color='orangered',linewidth=2,label='Regression Line')
mp.legend()
mp.show()