"""
demo04_cov.py 协方差
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
mp.figure('COV',facecolor='lightgray')
mp.title('COV',fontsize=16)
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
mp.plot(dates,bhp_closing_prices,color='dodgerblue',label='BHP')
mp.plot(dates,vale_closing_prices,color='orangered',label='VALE')

# 计算两支股票的协方差
ave_bhp = np.mean(bhp_closing_prices)
ave_vale = np.mean(vale_closing_prices)
# 离差
dev_bhp = bhp_closing_prices - ave_bhp
dev_vale = vale_closing_prices - ave_vale
# 协方差
cov = np.mean(dev_bhp * dev_vale)
print(cov)
# 相关系数
coef = cov /(np.std(bhp_closing_prices)*np.std(vale_closing_prices))
print(coef)
# 相关矩阵
m = np.corrcoef(bhp_closing_prices,vale_closing_prices)
print(m,m[0,1],m[1,0])
# 协方差矩阵
print(np.cov(bhp_closing_prices,vale_closing_prices))
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

