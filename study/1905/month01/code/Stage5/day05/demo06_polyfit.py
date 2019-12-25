"""
demo06_polyfit.py 多项式整合
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
dates,bhp_closing_prices = np.loadtxt('../da_data/bhp.csv',delimiter=',',usecols=(1,6),dtype='M8[D],f8',unpack=True,converters={1: dmy2ymd})
vale_closing_prices = np.loadtxt('../da_data/vale.csv',delimiter=',',usecols=(6,),unpack=True)

# 绘制收盘价的折线图
mp.figure('Polyfit',facecolor='lightgray')
mp.title('Polyfit',fontsize=16)
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
# 绘制差价函数曲线
diff_prices = bhp_closing_prices-vale_closing_prices
mp.plot(dates,diff_prices,color='dodgerblue',label='diff prices')
# 拟合差价函数
days = dates.astype('M8[D]').astype('int32')
P = np.polyfit(days,diff_prices,4)
poly_prices = np.polyval(P,days)
mp.plot(dates,poly_prices,color='orangered',label="Polyfit Line",linewidth=2)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

