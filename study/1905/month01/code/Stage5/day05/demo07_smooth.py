"""
demo07_smooth.py 数据平滑
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
dates,bhp_closing_prices = np.loadtxt('../da_data/bhp.csv',delimiter=',',usecols=(1,6),dtype='M8[D],f8',converters={1:dmy2ymd},unpack=True)
vale_closing_prices = np.loadtxt('../da_data/vale.csv',delimiter=',',usecols=(6),dtype='f8',converters={1:dmy2ymd},unpack=True)
bhp_returns = np.diff(bhp_closing_prices)/bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices)/vale_closing_prices[:-1]
dates = dates[:-1]
# 卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(bhp_returns,convolve_core,'valid')
vale_returns_convolved = np.convolve(vale_returns,convolve_core,'valid')
# 绘制这条曲线
mp.figure('BHP VALUE RETURNS',facecolor='lightgray')
mp.title('BHP VALUE RETURNS',fontsize=20)
mp.xlabel('Date')
mp.ylabel('Price')
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y %m %d'))
dates = dates.astype('M8[D]')
# 绘制收益线
mp.plot(dates,bhp_returns,color='dodgerblue',linestyle='--',label='bhp_returns',alpha=0.3)
mp.plot(dates,vale_returns,color='orangered',linestyle='--',label='vale_returns',alpha=0.3)
# 绘制卷积降噪线
mp.plot(dates[7:],bhp_returns_convolved,color='dodgerblue',label='bhp_returns_convolved',alpha=1)
mp.plot(dates[7:],vale_returns_convolved,color='orangered',label='vale_returns_convolved',alpha=1)
#拟合这两条曲线，获取两组多项式系数
days = dates.astype('M8[D]').astype('int32')
bhp_p = np.polyfit(days[7:], bhp_returns_convolved, 3)
bhp_polyfit_y = np.polyval(bhp_p, days[7:])
vale_p = np.polyfit(days[7:], vale_returns_convolved, 3)
vale_polyfit_y = np.polyval(vale_p, days[7:])
#绘制拟合线
mp.plot(dates[7:], bhp_polyfit_y, color='dodgerblue', label='bhp_returns_polyfit')
mp.plot(dates[7:], vale_polyfit_y, color='orangered', label='vale_returns_polyfit')
# 求取交点
diff_p = np.polysub(bhp_p,vale_p)
xs = np.roots(diff_p)
print(xs.astype('M8[D]'))
mp.show()
