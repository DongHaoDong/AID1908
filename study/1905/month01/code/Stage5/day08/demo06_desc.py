"""
demo06_desc.py  排序
"""
import pandas as pd
import numpy as np
# 创建DF
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack','Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,26,28,23,27,24]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,4.56,7.25,4.56,8.69,3.65,2.45,2.65,3.65])}
df = pd.DataFrame(d)
print(df)
print('---\n',df.mean())
print('---\n',df.mean(1))
print('---\n',df.max())
print('---\n',df.min())
print('---\n',df.count())
print('---\n',df.describe(include=['object','number']))