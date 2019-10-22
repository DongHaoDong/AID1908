"""
    使用range生成1 -- 10之间的数字
    将数字的平方存入list01中
    将list01中所有奇数存入list02中
    将list01中所有偶数存入list03中
    将list01中所有大于5的数字增加1后存入list04中
"""
# list01 = []
# for item in range(1, 11):
#     list01.append(item ** 2)
# print(list01)
# 将数字的平方存入list01中
list01 = [item ** 2 for item in range(1, 11)]
print(list01)
# 将list01中所有奇数存入list02中
# list02 = []
# for item in list01:
#     if item % 2 != 0:
#         list02.append(item)
# list02 = [item ** 2 for item in list01 if item % 2 != 0]
# print(list02)
# 将list01中所有偶数存入list03中
# list03 = []
# for item in list01:
#     if item % 2 == 0:
#         list03.append(item)
# list03 = [item ** 2 for item in list01 if item % 2 == 0]
# print(list03)
# 将list01中所有大于5的数字增加1后存入list04中
# list04 = []
# for item in list01:
#     if item % 2 == 0 and item > 5:
#         list04.append(item+1)
# print(list04)
# list04 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
# print(list04)