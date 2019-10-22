"""

"""
# 累加1--100之间的数字
sum_value = 0
# for item in range(1, 101):
#     满足条件执行累加
#     if item % 5 != 0:
#         continue
#     sum_value += item
for item in range(1, 101):
    # 不满足条件条过本次循环，继续执行下一次循环
    if item % 5 == 0:
        sum_value += item
print(sum_value)
