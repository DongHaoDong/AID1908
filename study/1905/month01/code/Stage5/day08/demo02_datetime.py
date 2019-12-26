"""
demo02_datetime.py      DateTimeIndex日期时间
"""
import pandas as pd
# 默认频率为D:（天）从10月1日连续生成7天
dates = pd.date_range('2019/10/01',periods=7)
print(dates,type(dates))
# 修改频率为M:（月）
dates = pd.date_range('2019/10/01',periods=7,freq='M')
print(dates,type(dates))
# 生成序列(工作日时间序列)
dates = pd.bdate_range('2019/12/26',periods=7)
print(dates)