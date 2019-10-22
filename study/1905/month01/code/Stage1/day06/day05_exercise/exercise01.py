"""
    计算列表中最小值(不使用min)
"""
list01 = [43, 54, 5, 4, 7, 8]
min_value = list01[0]
for item in list01:
    if min_value > item:
        min_value = item
print("列表{}中最小值是{}".format(list01, min_value))

