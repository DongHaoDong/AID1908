# 数据分析DAY03
## 填充
以某种颜色自动填充两条曲线的闭合区域
```
mp.fill_between(
    x,                      # x轴的水平坐标
    sin_x,                  # 下边界曲线上点的垂直坐标
    cos_x,                  # 上边界曲线上点的垂直坐标
    sin_x<cos_x,            # 填充条件,为True时填充
    color='',               # 填充颜色
    alpha=0.2               # 透明度
)
```
案例:绘制两条曲线：sin_x=sin(x) cos_x=cos(x/2)/2 [0-8π]
```python
import numpy as np
import matplotlib.pyplot as mp
n = 1000
x = np.linspace(0,8*np.pi,n)
sin_y = np.sin(x)
cos_y=np.cos(x / 2) / 2
mp.figure('Fill',facecolor='lightgray')
mp.title('Fill',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x,sin_y,color='dodgerblue',label=r'$y=sinx$')
mp.plot(x,cos_y,color='orangered',label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(x,sin_y,cos_y,sin_y>cos_y,color='dodgerblue',alpha=0.3)
mp.fill_between(x,sin_y,cos_y,sin_y<cos_y,color='orangered',alpha=0.3)
mp.legend()
mp.show()
```
## 条形图(柱状图)
绘制柱状图的相关API：
```
mp.figure('Bar',facecolor='lightgray')
mp.bar(
    x,              # 水平坐标数组
    y,              # 柱状图高度数组
    width,          # 柱子的宽度
    color='',       # 填充颜色
    label='',       # 图例文本
    alpha=0.2       # 透明度
)
```
案例：先以柱状图绘制苹果12个月的销量，然后再绘制句子的销量
```
import numpy as np
import matplotlib.pyplot as mp

apples = np.array([82,34,46,58,46,58,35,41,46,13,42,44])
oranges = np.array([69,76,23,84,61,25,21,34,82,69,12,34])

# 绘制柱状图
mp.figure('Bar',facecolor='lightgray')
mp.title('Bar Chart',fontsize=18)
mp.grid(linestyle=':')
x = np.arange(apples.size)
y = np.arange(oranges.size)
mp.bar(x-0.2,apples,0.4,color='limegreen',label='Apple',align='center')
mp.bar(y+0.2,oranges,0.4,color='orangered',label='Oranges',align='center')
# 设置刻度
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
mp.legend()
mp.show()
```
## 饼图
绘制饼状图的基本API
```
mp.pie(
    values,             # 值列表
    spaces,             # 扇形之间的间距列表
    labels,             # 标签列表
    colors,             # 颜色列表
    '%d%%',             # 标签所占比例格式
    shadow=True,        # 是否显示阴影
    startangle=90,      # 逆时针绘制饼状图时的起始角度
    radius=1            # 半径
)
```
案例:绘制饼状图显示5门语言的流行程度
```
mp.figure('pie',facecolor='lightgray')
# 整理数据
values = [26,17,21,29,11]
spaces = [0.05,0.01,0.01,0.01,0.01]
labels = ['Python','JavaScript','C++','Java','PHP']
colors = ['dodgerblue','orabgered','limegreen','violet','gold']
mp.figure('Pie',facecolor='lightgray')
mp.title('Pie',fontsize=20)
# 等轴比例
mp.axis('equal')
mp.pie(
    values,         # 值列表
    spaces,         # 标签列表
    colors,         # 颜色列表
    '%d%%',         # 标签所占比例格式
    shadow=True,    # 是否显示阴影
    startangle=90   # 逆时针绘制饼状图时的起始角度
    radius=1        # 半径
)
```
## 等高线
组成等高线需要网格点坐标矩阵,也需要每个点的高度。所以等高线属于3D数学模型范畴  
绘制等高线的相关API
```
import matplotlib.pyplot as mp
cntr = mp.contour(
    x,              # 网格坐标矩阵的x坐标(2为数组)
    y,              # 网格坐标矩阵的y坐标(2为数组)
    z,              # 网格坐标矩阵的z坐标(2为数组)
    8,              # 把等高线绘制成8部分
    color='black',  # 等高线的颜色
    linewidths=0.5  # 线宽
)
# 为登高线图添加高度标签
mp.clabel(cntr,inline_spacing=1,fmt='%.1f',fontsize=10)
mp.contourf(x,y,z,8,cmap='jet')
```
案例：生成网格坐标矩阵，并且绘制等高线
```
n=1000
# 生成网格化坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
mp.figure('Contour',facecolor='lightgray')
mp.title('Contour',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制等高线图
mp.contourf(x,y,z,8,cmcp='jet')
cntr = mp.contour(x,y,z,8,color='black',linewidths=0.5)
# 为登高线添加高度标签
mp.clabel(cntr,inline_spacing=3,fmt='%.1f%',fontsize=8)
mp.show()
```
## 热成像图
用图形的方式显示矩阵及矩阵中值的大小  
123  
456  
789  
绘制热成像图的相关API
```
# 把矩阵z图形化,使用cmap表示矩阵中每个元素的大小
# origin:坐标轴方向
# upper:缺省值
# lower:原点在左下角
mp.imshow(z,cmap='jet',origin='low')
```
使用颜色条显示热度值
```
mp.colorbar()
```
## 3D图像绘制
matplotlib支持绘制三维曲面。若希望绘制三维曲面，需要使用axes3d提供的3d坐标系。
```
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')  # class axes3d
```
matplotlib支持绘制三维点阵，三维曲面，三维线框图
```
ax3d.scatter(...)       # 绘制三维点阵
ax3d.plot_surface(...)  # 绘制三维曲面
ax3d.plot_wireframe(...)# 绘制三维线框图
```
3d散点图的绘制相关API
```
ax3d.scatter(
    x,                  # x轴坐标数组
    y,                  # y轴坐标数组
    marker='',          # 点型
    s=10,               # 大小
    zorder='',          # 图层序号
    color='',           # 颜色
    edgecolor='',       # 边缘颜色
    facecolor='',       # 填充色
    c=v,                # 颜色值根据cmap映射应用响应颜色
    cmap=''             # cmap
)
```
案例:随机生成三组坐标，程标准正态分布规则，并且绘制他们
```
n = 1000
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)
d = np.sqrt(x**2+y**2+z**2)
mp.figure('3D Scatter')
ax = mp.gca(projection='3d') # 创建三维坐标系
mp.title('3D Scatter',fontsize=20)
ax.set_xlabel=('x',fontsize=14)
ax.set_ylabel=('y',fontsize=14)
ax.set_zlabel=('z',fontsize=14)
mp.tick_params(labelsize=10)
ax.scatter(x,y,z,s=60,c=d,cmap='jet',alpha=0.5)
mp.show()
```
3d平面图绘制先关API
```
ax3d.plot_surface(
    x,              # 网格坐标矩阵的x轴坐标(2维数组)
    y,              # 网格坐标矩阵的y轴坐标(2维数组)
    z,              # 网格坐标矩阵的z轴坐标(2维数组)
    rstride=30,     # 行跨距
    cstride=30,     # 列跨距
    cmap='jet'      # 颜色映射
)
```
案例：绘制3d平面图
```
n = 1000
# 生成网格化坐标矩阵
x,y = np.meshgrid(np.linspace(-3,3,n),)
```
案例：3d线框图的绘制
```
# 绘制3D线框图
# rstride:行跨距
# cstride:列跨距
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30,linewidth=1,color='dodgerblue')
```
## 极坐标系
与笛卡尔坐标系不同，某些情况下极坐标系适合显示与角度有关的图像，例如雷达等，极坐标系可以描述极径ρ与极角θ的线性关系
```
mp.figure('Polar',facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar',fontsize=20)
mp.xlabel(r'$\theta$',fontsize=14)
mp.ylabel(r'$\rho$',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.show()
```
在极坐标系中绘制曲线
```
# 准备数据
t = np.linspace(0,4*np.pi,1000)
r = 0.8 * t
mp.plot(t,r)
mp.show()
```
案例:在极坐标系中绘制正弦函数。y=3 sin(6x)
```
x = np.linspace(0.6*np.pi,1000)
y = 3*np.sin(6*x)
mp.plot(x,y)
```
## 简单动画
动画即是在一段时间内快速连续的重新绘制图像的过程  
matplotlib提供了方法用于处理简单动画的绘制。定义update函数用于即时更新图像
```
import matplotlib.animation as ma
# 定义更新函数行为
def update(number):
    pass
# 每个10毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf():获取当前窗口
# update:更新函数
# interval:间隔时间(单位：毫秒)
anim = ma.FuncAnimation(mp.gcf(),update,interval=10)
mp.show()
```
案例：随机生成各种颜色的100个气泡，让他们不断的增大
```
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
```
在很多情况下，绘制动画的参数是动态获取的，matplotlib支持定义generator生成器函数，用于生成数据，把生成的数据交给update函数更新图像：
```
import matplotlib.animation as ma
# 定义更新函数行为
def update(data):
    t,v=data
    ...
    pass
def generator()
    yield t,v
# 每隔10毫秒将会先调用生成器。获取生成器返回的数据
# 把生成器返回的数据交给并调用update函数，再执行更新图像函数
anim = ma.FuncAnimation(ma.gcf(),update,generator.interval=10)
```
案例：绘制信号曲线：y=sin(2*π*t)*exp(sin(0.2*π*t)),数据通过生成器函数生成，在update函数中绘制曲线
```
mp.figure('Signal',facecolor='lightgray')
mp.title('Signal',fontsize=14)
mp.xlim(0,10)
mp.ylim(-3,3)
mp.grid(linestyle='--',color='lightgray',alpha=0.5)
pl=mp.plot([],[],color='dodgerblue',label='Signal')[0]
pl.set_data([],[])
x=0
def update(data):
    t,v=data
    x,y=pl.get_data()
    x.append(t)
    y.append(v)
    # 重新设置数据源
    pl.set_data(x,y)
    # 移动坐标轴
    if(x[-1]>10):
        mp.xlim(x[-1]-10,x[-1])
        
def y_generator():
    global x
    y = np.sin(2*np.pi*x)*np.exp(np.sin(0.2*np.pi*t))
    yield (x,y)
    x += 0.05
anim = ma.FuncAnimation(mp.gcf(),update,y_generator,interval=20)
mp.tight_layout()
map.show()
```
## 加载文件
numpy提供了函数用于加载逻辑上可被解释为二维数组的文本文件，格式如下
```
数据项1 <分隔符> 数据项2 <分隔符> ... 数据项n <分隔符>
例如:
AA,AA,AA,AA,AA
BB,BB,BB,BB,BB
...
或：
AA:AA:AA:AA:AA
BB:BB:BB:BB:BB
...
```
调用numpy.loadtxt()函数可以直接读取该文件并获取ndarray数组对象
```
import numpy as np
# 直接读取该文件并获取ndarray数组对象
# 返回值
    unpack=False:返回一个二维数组
    unpack=True:多个一维数组
np.loadtxt(
    '../aapl.csv',          # 文件路径
    delimiter=',',          # 分隔符
    usecols=(1,3),          # 读取1、3列(下标从0开始)
    unpack=False,           # 是否案列拆包
    dtype='u10, f8',        # 定制返回每一列数组中元素的类型
    convers={1:func}        # 转换器函数字典
)
```
案例：读取aapl.csv文件，得到文件中的信息
```
import numpy as np
import datetime as dt
# 日期转换函数
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t
dates, opening_prices,highest_prices, \
	lowest_prices, closeing_pric es  = np.loadtxt(
    '../data/aapl.csv',		# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3, 4, 5, 6),			# 读取1、3两列 （下标从0开始）
    unpack=True,
    dtype='M8[D], f8, f8, f8, f8',		# 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})
```
案例：使用matplotlib绘制K线图
1. 绘制dates与收盘价的折线图
```
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
# 绘制k线图，x为日期
mp.figure('APPL k',facecolor='lightgray')
mp.title('APPL k')
mp.xlabel('Day', fontsize=12)
mp.ylabel('Price', fontsize=12)
# 拿到坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器(每周一显示主刻度文本)
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())
mp.tick_params(labelsize=8)
dates = dates.astype(md.datetime.datetime)
mp.plot(dates,opening_prices,color='dodgerblue',linestyle='-')
mp.gcf().autofmt_xdate()
mp.show()
```
2. 每日蜡烛图
```
#绘制每一天的蜡烛图
#填充色：涨为白色，跌为绿色
rise = closeing_prices >= opening_prices
color = np.array([('white' if x else 'limegreen') for x in rise])
#边框色：涨为红色，跌为绿色
edgecolor = np.array([('red' if x else 'limegreen') for x in rise])

#绘制线条
mp.bar(dates, highest_prices - lowest_prices, 0.1,
	lowest_prices, color=edgecolor)
#绘制方块
mp.bar(dates, closeing_prices - opening_prices, 0.8,
	opening_prices, color=color, edgecolor=edgecolor)
```
