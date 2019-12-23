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
a = np.array(data,dtype='U2, 3int32, int32')
print(a)
print(a[1][1])