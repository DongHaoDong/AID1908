"""
demo04_dataframe.py DataFrame基本操作
"""
import pandas as pd
import numpy as np

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
# 列访问
print(df['one'])
print(df[['one', 'two']])
# 列添加
df['three'] = pd.Series([2,3,4,5],index=['a','b','c','d'])
df['three'] = pd.Series([2,3,4,5],index=df.index)
print(df)
# 列的删除
del(df['one'])
print(df)
df.pop('two')
print(df)
# 行访问   使用切片的方式访问
df = pd.DataFrame(d)
print(df)
print(df[2:])
print(df.loc['a'])
print(df.loc[['a','b']])
# iloc    接收下标索引
print(df.iloc[1])
print(df.iloc[[1,2]])
print(df.iloc[1,1])
# 行添加
data = np.array([['zs',18],['ls',20]])
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
data = np.array([['ww',19],['zl',21]])
df2 = pd.DataFrame(data,columns=['Nick','Score'])
print(df2)
df = df.append(df2)
print(df)
# 删除行
# df = df.drop(0)
# print(df)
# 修改元素
df['Nick'][0] = 'Nick'
print(df)
df.iloc[0]['Nick'] = 'Tom'
print(df)

