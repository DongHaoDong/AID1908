"""
demo04_profit.py    定义一种买入卖出策略，使用历史数据进行验证，这种策略是否可以试试
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

def profit(open,high,low,close):
    # 定义买入卖出策略计算当天收益率
    buying_price = open * 0.99
    if (low<buying_price<high):
        return (close-buying_price)/buying_price
    else:
        return np.nan
# 矢量化profit函数，求得30天的收益率
profits = np.vectorize(profit)(
    opening_prices,highest_prices,lowest_prices,closing_prices)
print(profits)
isnan_mask = np.isnan(profits)
dates = dates[~isnan_mask]   # 非nan的日期
profits = profits[~isnan_mask]  # 非nan的收益率
# 绘制收盘价的折线图
mp.figure('Profits',facecolor='lightgray')
mp.title('Profits',fontsize=16)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Profits',fontsize=14)
mp.grid(linestyle=':')
#拿到坐标轴
ax = mp.gca()
#设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator( md.WeekdayLocator(byweekday=md.MO) )
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
#设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())
print(profits.mean())
dates = dates.astype(md.datetime.datetime)
mp.plot(dates,profits,'o-',color='dodgerblue',label='profits',linewidth=2)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

