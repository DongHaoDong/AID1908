"""
demo10_anim.py
"""
import matplotlib.pyplot as mp
import matplotlib.animation as ma
import numpy as np

# 随机生成100个对象
n = 100
balls = np.zeros(100,dtype=np.dtype([
    ('position',float,2),   # 位置(水平和垂直坐标)
    ('size',float,1),       # 大小
    ('growth',float,1),     # 生长速度
    ('color',float,4)       # 颜色(红,绿,蓝和透明度)
]))
# 初始化balls数组每个字段的属性值
balls['position']=np.random.uniform(0,1,(n,2))
# for ball in balls:
#     print(ball)
balls['size']=np.random.uniform(50,70,n)
balls['growth']=np.random.uniform(10,20,n)
balls['color']=np.random.uniform(0,1,(n,4))
# 画图
mp.figure("Animation",facecolor='lightgray')
mp.title("Animation",fontsize=16)
mp.xticks([])
mp.yticks([])
sc = mp.scatter(
    balls['position'][:,0],
    balls['position'][:,1],
    balls['size'],
    color=balls['color']
)

def update(number):
    # 选择一个点
    index = number % 100
    # 重新修改index位置元素的属性
    balls['position'][index] = np.random.uniform(0,1,(1,2))
    balls['size'][index] = np.random.uniform(50,70,1)
    balls['size'] += balls['growth']
    # 重新绘制
    sc.set_sizes(balls['size']) # 更新大小
    sc.set_offsets(balls['position']) # 更新位置

# 动起来
anim = ma.FuncAnimation(mp.gcf(),update,interval=30)
mp.show()