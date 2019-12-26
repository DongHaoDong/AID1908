"""
demo08_groupby.py  分组
"""
import pandas as pd
import numpy as np
ipl_data = {'Team':['Riders','Riders','Devils','Devils','Kings','Kings','Kings','kings','Riders','Royals','Riders','Royals'],'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
# 按照年份Year字段分组
grouped=df.groupby('Year')
print(grouped)
# 查看分组结果
print(grouped.groups)
for year,group in grouped:
    print(year)
    print(group)
g2014=grouped.get_group(2014)
print(g2014)
# 聚合函数
print(grouped['Points'].agg(np.mean))
print(grouped['Points'].agg([np.mean,np.max,np.min,np.std]))
print(df.values)