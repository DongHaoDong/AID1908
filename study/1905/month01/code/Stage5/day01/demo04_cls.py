"""
demo04_cls.py  数据类型
"""
import numpy as np

data=[
    ('zs',[80,60,75],19),
    ('ls',[99,97,86],20),
    ('ww',[98,98,98],21)
]
# 第一种设置dtype的方式
a = np.array(data,dtype='U3, 3int32, int32')
print(a)
print(a[1][1])
# 第二种设置dtype的方式
a = np.array(
    data,dtype=[('name', 'str_', 2),
                ('score', 'int32', 3),
                ('age', 'int32', 1)])
print(a)
print(a[2]['age'])
# 第三种设置dtype的方式
a = np.array(
    data,dtype={'names': ['name', 'score', 'age'],
                'formats': ['U3','3int32','int32']})
print(a)
print(a[1]['name'])
# 测试数组中存储日期数据类型
print("####################################################################")
dates = ['2011-01-01','2011','2011-02','2012-01-01','2012-02-01 10:10:00']
dates = np.array(dates)
# 类型转换
dates = dates.astype('M8[D]')
print(dates,dates.dtype)
print(dates[2] - dates[1])
dates = dates.astype('int32')
print(dates)
