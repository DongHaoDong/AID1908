"""
demo01_boll.py 布林带
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
mp.plot(dates,closing_prices,color='dodgerblue',label='APPL',linestyle='--',linewidth=2,alpha=0.5)
# 加权卷积实现5日均线
x = np.linspace(-1,0,5)
kernel = np.exp(x)[::-1]
kernel = kernel / kernel.sum()
ma53 = np.convolve(closing_prices,kernel,'valid')
mp.plot(dates[4:],ma53,color='orangered',label='MA-53')
# 计算上轨与下轨
stds = np.zeros(ma53.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i+5].std()
upper = ma53 + 2 * stds
lower = ma53 - 2 * stds
mp.plot(dates[4:],upper,color='red',label='UPPER')
mp.plot(dates[4:],lower,color='red',label='LOWER')
mp.fill_between(dates[4:],upper,lower,lower<upper,color='orangered',alpha=0.3)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

