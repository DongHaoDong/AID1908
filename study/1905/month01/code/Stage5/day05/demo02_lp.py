"""
demo02_lp.py 线性预测
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
mp.plot(dates,closing_prices,color='dodgerblue',label='APPL',linestyle='--',linewidth=2)

# 线性预测
# 整理A与B
N=3
pred_prices = np.zeros(30-N*2)
for i in range(pred_prices.size):
    A = np.zeros((N, N))
    for j in range(N):
        A[j,] = closing_prices[i+j:i+j + N]
    B = closing_prices[i+N:i+N*2]
    x = np.linalg.lstsq(A, B)[0]
    pred = B.dot(x)  # 点乘 两数组对应位置相乘再相加
    pred_prices[i] = pred
mp.plot(dates[N*2:],pred_prices,'o-',color='orangered',label="Prediction")
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

