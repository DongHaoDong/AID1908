"""
    在列表[54,25,12,42,35,17]中,选出最大值
"""
numbers = [54, 25, 12, 42, 35, 17]
max_value = numbers[0]
for item in numbers:
    if max_value < item:
        max_value = item
print("列表{}中最大值是{}".format(numbers, max_value))