"""
demo06_splice.py 切片操作
"""
import numpy as np
a = np.arange(1,10)
print(a)    # 1 2 3 4 5 6 7 8 9
print(a[:3])    # 1 2 3
print(a[3:6])   # 4 5 6
print(a[6:])    # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])   # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])   # 3 6 9

# 二维数组切片
a.resize(3,3)
print(a)
print(a[::2,:])
print(a[::2,::2])