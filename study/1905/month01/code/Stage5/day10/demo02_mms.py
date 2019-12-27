"""
demo01_scale.py   范围缩放
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17.,90.,4000.],
    [20.,80.,5000.],
    [23.,75.,5500.]])
mms = sp.MinMaxScaler(feature_range=(0,1))
result = mms.fit_transform(raw_samples)
print(result)
print(result.mean(axis=0))
print(result.std(axis=0))

# 手动计算
new_samples = []
for row in raw_samples.T:
    min_val = row.min()
    max_val = row.max()
    # 整理求出缩放线性关系所需要的矩阵:A与B
    A = np.array([[min_val,1],[max_val,1]])
    B = np.array([0,1])
    # x = np.linalg.lstsq(A,B)[0]
    x = np.linalg.solve(A,B)
    new_row = row * x[0] + x[1]
    new_samples.append(new_row)
print(np.array(new_samples).T)