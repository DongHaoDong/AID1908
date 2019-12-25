"""
demo01_k.py 绘制k线图
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
mp.plot(dates,closing_prices,color='dodgerblue',label='APPL',linestyle='--',linewidth=2,alpha=0.3)
# 绘制蜡烛图
# 整理颜色
rise = closing_prices > opening_prices
# color = [' white' if x else 'green' for x in rise]
color = np.zeros(rise.size,dtype='U5')
color[:] = 'green'
color[rise] = 'white'
# 边缘色
ecolor = ['red' if x else 'green' for x in rise]
# 绘制实体
mp.bar(dates,closing_prices-opening_prices,0.8,opening_prices,color=color,edgecolor=ecolor,zorder=3)
# 绘制影线图
mp.vlines(dates,lowest_prices,highest_prices,color=ecolor)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

