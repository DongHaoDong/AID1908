"""
demo07_ma.py 移动均线
"""
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

# 卷积实现五日移动均线
kernel = np.ones(5)/5
m52 = np.convolve(closing_prices,kernel,'valid')
mp.plot(dates[4:],m52,color='red',alpha=0.3,linewidth=7,label='SMA-52')
# 卷积实现十日移动均线
kernel = np.ones(10)/10
m10 = np.convolve(closing_prices,kernel,'valid')
mp.plot(dates[9:],m10,color='green',label='MA-10')
# 加权卷积实现5日均线
x = np.linspace(-1,0,5)
kernel = np.exp(x)[::-1]
kernel = kernel / kernel.sum()
m53 = np.convolve(closing_prices,kernel,'valid')
mp.plot(dates[4:],m53,color='black',label='MA-53')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

