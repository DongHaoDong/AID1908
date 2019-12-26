"""
demo07_sort     排序
"""
import pandas as pd
import numpy as np
unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)
print(unsorted_df.sort_index())
print(unsorted_df.sort_index(axis=1))
print(unsorted_df.sort_index(ascending=False))

# 按照某个字段值进行排序
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack','Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,26,28,23,27,24]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,4.56,7.25,4.56,8.69,3.65,2.45,2.65,3.65])}
unsorted_df=pd.DataFrame(d)
print('---\n',unsorted_df)
# 按照年龄进行排序
sorted_age = unsorted_df.sorted_values(by='Age',ascending=False)
print(sorted_age)
# 先按照年龄进行排序，然后按照Rating降序排序
sorted_age_rating = unsorted_df.sorted_values(by=['Age','Rating'],ascending=[True,False])
print(sorted_age_rating)