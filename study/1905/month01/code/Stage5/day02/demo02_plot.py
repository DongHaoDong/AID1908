"""
demo02_plot.py
"""
import numpy as np
import matplotlib.pyplot as mp

# 线型拆分1000个点
x = np.linspace(-np.pi,np.pi,1000)
# print(x,x.shape)
sinx = np.sin(x)
# 余弦曲线cos(x) / 2
cosx = np.cos(x) / 2
# 设置坐标轴的范围
# mp.xlim(0,np.pi)
# mp.ylim(0,1)
# 修改x轴的刻度文本
vals = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
texts = [r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(vals,texts)
# 修改坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
mp.yticks([-1.0,-0.5,0.5,1.0])
mp.plot(x,sinx,linestyle='--',linewidth=2,color='orangered',alpha=0.8,label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle='-.',linewidth=2,color='dodgerblue',alpha=0.9,label=r'$y=\frac{1}{2}cos(x)$')
# 绘制特殊点
pointx = [np.pi / 2,np.pi / 2]
pointy = [1,0]
mp.scatter(pointx,pointy,marker='o',s=70,color='red',label='smaple points',zorder=3)

mp.annotate(
    r'$[\frac{\pi}{2},1]$',         # 备注中显示的文本内容
    xycoords='data',                # 备注目标点所使用的坐标系(data百世数据坐标系)
    xy=(np.pi / 2,1),               # 备注目标点的坐标
    textcoords='offset points',     # 备注文本所使用的坐标系(offset points表示参照点的偏移坐标系)
    xytext=(50,30),                   # 备注文本的坐标
    fontsize=14,                    # 备注文本的字体大小
    arrowprops=dict(
        arrowstyle='-|>',
        connectionstyle='bar')               # 使用字典定义文本指向目标点的箭头样式
)

mp.legend()
mp.show()


