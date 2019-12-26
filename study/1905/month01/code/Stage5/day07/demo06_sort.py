"""
demo06_sort.py  排序
"""
import numpy as np
import matplotlib.pyplot as mp

names = np.array(['Apple','Huawei','Mi','Oppo','Vivo'])
prices = np.array([8888,5888,2999,3999,3999])
volumes = np.array([60,110,40,50,70])
# 排序    先按价格排序，然后按销量排序
indices = np.lexsort((-volumes,prices))
print(names[indices])

print('-'*45)

a = np.array([1,3,4,5,7,9])
b = np.array([6,8])
# 寻找向a中的那些位置，插入b中的元素
indices = np.searchsorted(a,b)
print(indices)
# 插入元素 向a中的indices位置插入b元素
c = np.insert(a,indices,b)
print(c)