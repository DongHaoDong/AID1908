"""
demo06_func.py  通用函数
"""
import numpy as np

a = np.arange(1,10)
print(a)
# 裁剪
print(np.clip(a,3,7))
print(a.clip(min=3,max=7))
# 压缩(只保留a>5的元素)

mask=np.all([a>3,a<7],axis=0)
print(a.compress(mask))
print(a.compress(a>5))
print(a[a>5])