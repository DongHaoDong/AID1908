"""
demo03_max.py 求最值
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

# 评估波动性
min_val = np.min(lowest_prices)
max_val = np.max(highest_prices)
print(min_val,'~',max_val)
# 获取最高价与最低价的日期
min_ind = np.argmin(lowest_prices)
max_ind = np.argmax(highest_prices)
print('min:',dates[min_ind])
print('max:',dates[max_ind])
# maximum minimum
a = np.arange(1,10).reshape(3,3)
b = np.arange(1,10)[::-1].reshape(3,3)
print(a)
print(b)
print(np.maximum(a,b))
print(np.minimum(a,b))