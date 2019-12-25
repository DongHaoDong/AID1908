# 数据分析Day04
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
## 算数平均值
```
s = [s1,s2,,...,sn]
```
样本中的每个值都是真值与误差的和
```
算数平均值
m = (s1+s2+...+sn) / n
```
算数平均值表示对真值的无偏估计
```
np.mean(array)
array.mean()
```
案例:计算收盘价的算数平均值
```
import numpy as np
closing_prices = np.loadtxt('../../data/aapl.csv',delimiter=',',usecols=(6),unpack=True)
mean = 0
for closing_price in closing_prices:
    mean += closing_price
mean /= closing_prices.size
print(mean)
mean = np.mean(closing_price)
print(mean)
```
## 加权平均值
样本：S=[S1,S2,...,Sn]
权重:W=[W1,W2,...,Wn]
加权平均值:a=(S1W1+S2W2+...+SnWn)/(W1+W2+...+Wn)
```
np.average(closing_prices,weights=volumes)
```
VWAP-成交量加权平均价格(成交量体现了市场对当前交易价格的认可度，成交量加权平均价格将会更接近这支股票的真实价值)
```
import numpy as np
closing_prices, volumes = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6, 7), unpack=True)
vwap, wsum = 0, 0
for closing_price, volume in zip(
        closing_prices, volumes):
    vwap += closing_price * volume
    wsum += volume
vwap /= wsum
print(vwap)
vwap = np.average(closing_prices, weights=volumes)
print(vwap)
```
## TWAP - 时间加权平均价格（时间越晚权重越高，参考意义越大）
```
import datetime as dt
import numpy as np

def dmy2days(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    days = (date - dt.date.min).days
    return days

days, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    converters={1: dmy2days})
twap = np.average(closing_prices, weights=days)
print(twap)
```
## 最值
np.max(),np.min(),np.ptp():返回一个数组中最大值/最小值/极差
```
import numpy as np
# 产生9个介于[10,100]区间的随机数
a = np.random.randint(10,100,9)
print(a)
print(np.max(a),np.min(a),np.ptp(a))
```
np.argmax(),np.argmin():返回一个数组中最大/最小元素的下标
```
print(np.argmax(a),np.argmin(a))
```
np.maximum(),np.minimum():将两个同维数组中对应元素中最大/最小元素构成一个新的数组
```
print(np.maximum(a,b),np.minimum(a,b),sep='\n')
```
案例：评估AAPL股票的波动性
```
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')
    time = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t
dates,opening_prices,highest_prices,lowest_prices,closing_prices,volumes = np.loadtxt('../da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6,7),dtype='M8[D],f8,f8,f8,f8,f8',unpack=True,converters={1: dmy2ymd})

# 评估波动性
min_val = np.min(lowest_prices)
max_val = np.max(highest_prices)
print(min_val,'~',max_val)
# 获取最高价与最低价的日期
min_ind = np.argmin(lowest_prices)
max_ind = np.argmax(highest_prices)
print('min:',dates[min_ind])
print('max:',dates[max_ind])
# maximum minimum
a = np.arange(1,10).reshape(3,3)
b = np.arange(1,10)[::-1].reshape(3,3)
print(a)
print(b)
print(np.maximum(a,b))
print(np.minimum(a,b))
```
## 中位数
将多个样本按照大小排序，取中间位置元素  
若样本数量为奇数，中位数为最中间的元素  
1 2000 3000 4000 10000000  
若样本数量为偶数，中位数为最中间的两个元素的平均值  
1 2000 3000 4000 5000 10000000  
案例：分析中位数的算法，测试numpy提供的中位数API
```
import numpy as np
closing_prices=np.loadtxt('../../data/aapl.csv',delimiter=',',usecols=(6),unpack=True)
size = closing_prices.size
sorted_prices = np.msort(closing_prices)
median=(sorted_prices[int((size-1)/2)]+sorted_prices[int(size/2)]) / 2
print(median)
median = np.median(closing_prices)
print(median)
```
## 标准差
样本：S = [s1,s2,...,sn]
平均值:m=(s1+s2+...+sn)/n
离差:D=[d1,d2,...,dn],di=si-m
离差方:Q=[q1,q2,...,1n],qi = di^2
总体方差:v=(q1+q2+...+qn)/n
总体标准差:s=sqrt(v),方均根
样本方差:v'=(q1+q2+...+qn)/(n-1)
样本标准差:s'=sqrt(v'),方均根
```
import numpy as np
closing_prices=np.loadtxt(
    '../../data/aapl.csv',delimiter=',',usecols=(6),unpack=True)
mean = np.mean(closing_prices)      # 算数平均值
devs = closing_prices-mean          # 离差
dsgs = devs ** 2                    # 离差方
pvar = np.sum(dsqs) / dsqs.size     # 总体方差
pstd = np.sqrt(pvar)                # 总体标准差
svar = np.sum(dsqs) / (dsqs.size-1) # 样本方差
sstd = np.sqrt(svar)                # 样本标准差
print(pstd,sstd)
pstd = np.std(closing_prices)       # 总体标准差
sstd = np.std(closing_prices,ddof=1)# 样本标准差
print(pstd,sstd)
```
## 时间数据处理
案例：统计每个周一、周二、...、周五的收盘价的平均值，并放入一个数组
```
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')
    time = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    t = time.weekday()
    return t
wdays,opening_prices,highest_prices,lowest_prices,closing_prices,volumes = np.loadtxt('../da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6,7),unpack=True,converters={1: dmy2ymd})

ave_prices = np.zeros(5)
for i in range(ave_prices.size):
    ave_prices[i]=np.mean(closing_prices[wdays==i])
print(ave_prices)
```
## 数组的轴向汇总
案例：汇总每周的最高价，最低价，开盘价，收盘价
```
def func(data):
    pass
# func          # 处理函数
#axis           # 轴向 [0,1]
np.apply_along_axis(func,axis,array)
```
沿着数组中所指定的轴向，调用处理函数，并将每次调用的返回值重新组成数组返回
## 移动均线
收盘价5日均钱：从第五天开始，每天计算最近五天的收盘价的平均值所构成的一条线  
移动均线算法：  
```
(a+b+c+d+e)/5
(b+c+d+e+f)/5
(c+d+e+f+g)/5
...
(f+g+h+i+j)/5 
```
在K线图中绘制5日均线图
```
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')
    time = dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t
dates,opening_prices,highest_prices,lowest_prices,closing_prices = data = np.loadtxt('../da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6),dtype='M8[D],f8,f8,f8,f8',unpack=True,converters={1: dmy2ymd})

# 绘制收盘价的折线图
mp.figure('AAPL',facecolor='lightgray')
mp.title('AAPL',fontsize=16)
mp.xlabel('Date',fontsize=14)
mp.ylabel('closing price',fontsize=14)
mp.grid(linestyle=':')
#拿到坐标轴
ax = mp.gca()
#设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator( md.WeekdayLocator(byweekday=md.MO) )
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
#设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())
dates = dates.astype(md.datetime.datetime)
mp.plot(dates,closing_prices,color='dodgerblue',label='APPL',linestyle='--',linewidth=2,alpha=0.6)
# 绘制移动均线
ma5 = np.zeros(closing_prices.size - 4)
for i in range(ma5.size):
    ma5[i] = closing_prices[i:i+5].mean()
mp.plot(dates[4:],ma5,color='orangered',label='MA-5')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```
## 卷积
激励函数:g(t)  
单位激励下的响应函数:f(t)  
绘制时间(t)与痛感(h)的函数关系图
```
a = [1 2 3 4 5] 原数组
b = [6 7 8]     卷积核数组
使用b作为卷积核，对a数组执行卷积运算的运算过程如下:
            44 65 86        有效卷积(valid)
         23 44 65 86 59     同维卷积(same)
      8  23 44 65 86 59 30  完全卷积(full)
0  0  1  2  3  4  5  0  0
6  7  8
   6  7  8  
      6  7  8
         6  7  8
            6  7  8
               6  7  8
                  6  7  8
c = numpy.convolve(a,b,卷积类型)
```
5日移动均线序列可以直接使用卷积实现
```
a = [a,b,c,d,e,f,g,h,i,j]
b = [1,5,1/5,1/5,1/5,1/5]
```
使用卷积函数numpy.convolve(a,b,卷积类型)实现5日均线
```
sma52 = np.convolve(closing_prices,np.ones(5)/5,'valid')
mp.plot(dates[4:],sma52,c='limegreen',alpha=0.5,linewidth=6,label='SMA-5(2)')
```
使用卷积函数numpy.convolve(a,b,卷积类型)实现10日均线
```
sma10 = np.convolve(closing_prices,np.ones(10)/10,'valid')
mp.plot(dates[9:],sma10,c='dodgerblue',linewidth=6,label='SMA-10')
```
使用卷积函数numpy.convolve(a,b,卷积类型)实现加权5日均钱
```
weights = np.exp(np.linspace(-1,0,5))
weights /= weights.sum()
ema5 = np.convolve(closing_prices,weights[::-1],'valid')
mp.plot(dates[4:],ema5,c='limegreen',alpha=0.5,linewidth=6,label='SMA-5')
```



