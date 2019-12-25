"""
demo04_median.py 中位数
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
dates,opening_prices,highest_prices,lowest_prices,closing_prices,volumes = np.loadtxt('../da_data/aapl.csv',delimiter=',',usecols=(1,3,4,5,6,7),dtype='M8[D],f8,f8,f8,f8,f8',unpack=True,converters={1: dmy2ymd})

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
mp.plot(dates,closing_prices,color='dodgerblue',label='APPL',linestyle='--',linewidth=2)
# 求算数平均数
mean = np.mean(closing_prices)
mean = closing_prices.mean()
mp.hlines(mean,dates[0],dates[-1],color='green',label='Mean')
# VWAP
vwap = np.average(closing_prices,weights=volumes)
mp.hlines(vwap,dates[0],dates[-1],color='red',label='VWAP')
# TWAP
times = np.linspace(1,10,closing_prices.size)
twap = np.average(closing_prices,weights=times)
mp.hlines(twap,dates[0],dates[-1],color='blue',label='TWAP')
# 中位数
median = np.median(closing_prices)
mp.hlines(median,dates[0],dates[-1],color='violet',label='median')
# 自己算
sorted_prices = np.msort(closing_prices)
size = sorted_prices.size
m = (sorted_prices[int((size-1)/2)] + sorted_prices[int(size/2)])/2
print(median,'~',m)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()



