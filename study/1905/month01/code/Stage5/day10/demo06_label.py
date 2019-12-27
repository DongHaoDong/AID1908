"""
demo06_label.py     标签编码器
"""
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'ford', 'redflag',
    'audi'])
print(raw_samples)
# 训练之前,需要标签编码
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)
# 假设训练之后得到一组测试样本的结果
test = [0,0,1,1,4]
print(lbe.inverse_transform(test))