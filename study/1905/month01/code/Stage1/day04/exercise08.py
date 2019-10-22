"""
    累加10-50之间个位不是2,5,9的整数
"""
sum_value = 0
for item in range(10, 51):
    unit = item % 10
    # 个位是2,5,9的整数则跳过
    if unit == 2 or unit == 5 or unit == 9:
        continue
    sum_value += item
