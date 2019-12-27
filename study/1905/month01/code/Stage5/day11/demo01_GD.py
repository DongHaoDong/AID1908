"""
demo01_GD.py    梯度下降实现线性回归
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import art3d

train_x = np.array([0.5,0.6,0.8,1.1,1.4])
train_y = np.array([5.0,5.5,6.0,6.8,7.0])

w0,w1,losses,epoches = [1],[1],[],[]
times = 1000
lrate = 0.01
for i in range(1,times+1):
    epoches.append(i)
    # 求损失值
    loss = ((w0[-1]+w1[-1]*train_x-train_y)**2).sum()/2
    losses.append(loss)
    print('{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(i, w0[-1], w1[-1], loss))
    # 求损失函数关于w0与w1的偏导数，从而更新模型参数
    d0 = (w0[-1]+w1[-1]*train_x-train_y).sum()
    d1 = (train_x*(w0[-1]+w1[-1]*train_x-train_y)).sum()
    # 根据梯度下降公式,更新w0与w1
    w0.append(w0[-1] -lrate * d0)
    w1.append(w1[-1] -lrate * d1)
print('w0:',w0[-1])
print('w1:',w1[-1])
# 绘制回归线
linex = np.linspace(train_x.min(),train_y.max(),100)
liney = w1[-1] * linex + w0[-1]
# 画图
mp.figure('Linear Regression',facecolor='lightgray')
mp.title('Linear Regression',fontsize=18)
mp.grid(linestyle=':')
mp.scatter(train_x,train_y,s=80,marker='o',color='dodgerblue',label='Samples')
mp.plot(linex,liney,color='orangered',linewidth=2,label='Regression Line')
mp.legend()
# 训练过程图 绘制w0 w1 loss的变化曲线
mp.figure('Training Process',facecolor='lightgray')
mp.title('Training Process',fontsize=18)
mp.subplot(311)
mp.grid(linestyle=":")
mp.ylabel(r'$w_0$',fontsize=14)
mp.plot(epoches,w0[:-1],color='dodgerblue',label=r'$w_0$')
mp.legend()
mp.tight_layout()
mp.subplot(312)
mp.grid(linestyle=":")
mp.ylabel(r'$w_1$',fontsize=14)
mp.plot(epoches,w1[:-1],color='dodgerblue',label=r'$w_1$')
mp.legend()
mp.tight_layout()
mp.subplot(313)
mp.grid(linestyle=":")
mp.ylabel(r'$loss$',fontsize=14)
mp.plot(epoches,losses,color='orangered',label=r'$loss$')
mp.legend()
mp.tight_layout()
# 绘制三维曲面图，显示梯度下降过程
n = 500
w0_grid,w1_grid = np.meshgrid(np.linspace(0,9,n),np.linspace(0,3.5,n))
loss_grid=0
for x,y in zip(train_x,train_y):
    loss_grid += (w0_grid+w1_grid*x-y)**2/2
mp.figure('Loss Function',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0')
ax3d.set_ylabel('w1')
ax3d.set_zlabel('loss')
ax3d.plot_surface(w0_grid,w1_grid,loss_grid,cstride=30,rstride=30,cmap='jet')
ax3d.plot(w0[:-1],w1[:-1],losses,'o-',color='red')
mp.tight_layout()
# 以等高线的方式绘制梯度下降的过程
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('w0', fontsize=14)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(w0_grid, w1_grid, loss_grid, 10, cmap='jet')
cntr = mp.contour(w0_grid, w1_grid, loss_grid, 10,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()
mp.tight_layout()
mp.show()