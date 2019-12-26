"""
demo03_DateFrame.py DataFrame结构
"""
import pandas as pd
# 创建一个空DataFrame
df = pd.DataFrame()
print(df,type(df))
# 通过列表数据创建DataFrame
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
# 通过二维列表创建DataFrame
data = [[80,81],[70,71],[80,81],[90,91],[60,61]]
df = pd.DataFrame(data)
print(df)
# 创建DataFrame的同时，设置列索引标签
df = pd.DataFrame(data,columns=['yuwen','shuxue'],index=['zs','ls','ww','zl','tq'])
print(df)
# 通过列表创建DataFrame
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data)
print(df)
# 从字典来创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)