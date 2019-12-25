"""
demo06_weekday.py 日期时间处理
"""
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


# 二维数组的轴向汇总
ary = np.arange(1,37).reshape(6,6)
print(ary)
def apply(data):
    # 汇总算法
    return data.mean(),data.min(),data.max()
r = np.apply_along_axis(apply,0,ary)
print(r)