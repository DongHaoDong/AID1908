"""
    列表推导式
"""
# list01中的元素，增加1后存入list02列表中
list01 = [5, 56, 6, 7, 7, 18, 19]
# list02 = []
# for item in list01:
#     list02.append(item+1)
# print(list02)
# list02 = [item + 1 for item in list01]
# print(list02)
# list01中大于10的元素，增加1后存入list02列表中
# for item in list01:
#     if item > 10:
#         list02.append(item+1)
# print(list02)
list02 = [item + 1 for item in list01 if item > 10]
print(list02)