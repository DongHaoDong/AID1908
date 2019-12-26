"""
demo05_random.py    随机数
"""
import numpy as np

print(np.random.binomial(10,0.3,100))

# 投10次，每次命中0.3,进球3的概率
a = np.random.binomial(10,0.3,100000)
for i in range(11):
    print('P(',i,'):',(a==i).sum() / 100000)

# 超几何分布
# 7个好苹果，3个坏苹果，随机抽三3个，求概率
a = np.random.hypergeometric(7,3,3,100000)
print('P(0)',(a==0).sum() / 100000)
print('P(1)',(a==1).sum() / 100000)
print('P(2)',(a==2).sum() / 100000)
print('P(3)',(a==3).sum() / 100000)
