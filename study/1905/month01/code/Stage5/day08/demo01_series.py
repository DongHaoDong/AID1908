"""
demo01_series.py    Series对象
"""
import pandas as pd
import numpy as np

# 创建Series对象
s = pd.Series()
print(s,type(s),s.dtype)

# 通过ndarray创建Series
ary = np.array([70,80,90,95])
s = pd.Series(ary)
print(s)
# 创建Series对象时，指定index行级索引标签
s = pd.Series(ary,index=['zs','ls','ww','zl'])
print(s,s['zs'])
# 通过字典创建Series
dic = {'zs':80,'ww':75,'tq':60,'wb':100}
s = pd.Series(dic)
print(s)
# 通过标量创建Series
s = pd.Series(1/5, index=np.arange(5))
print(s)
# 访问Series元素
print("-"*50)
s = pd.Series(ary,index=['zs','ls','ww','zl'])
print(s)
print(s[3])
print(s['zl'])
print(s[1:])
print(s[['ls','ww','zl']])
# 测试pandas的日期处理
# 构架日期类型的Series
dates = pd.Series(['2011','2011-02','2011-03-01','2011/04/01','2011/05/01 01:01:01','01 Jun 2011'])
# to_datetime()转换日期数据类型
dates = pd.to_datetime(dates)
print(dates,dates.dtype,type(dates))
# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('2011-01-01')
print(delta)
# 获取天数数量
print(delta.dt.days)
print(dates.dt.dayofweek)