"""
    字典推导式
"""
# 1 2 3 4 5 6 7 8 9 10 --> 平方
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2
print(dict01)
# 推导式
dict02 = {item: item ** 2 for item in range(1, 11)}
print(dict02)
# 只记录大于5的数字
dict01 = {}
for item in range(1, 11):
    if item > 5:
        dict01[item] = item ** 2
print(dict01)
# 推导式
dict03 = {item: item ** 2 for item in range(1, 11) if item > 5}
print(dict03)

