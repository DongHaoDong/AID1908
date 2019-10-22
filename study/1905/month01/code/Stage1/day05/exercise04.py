"""
    将列表[54,25,12,42,35,17]中大于30的存入到另外一个列表中
"""
list01 = [54, 25, 12, 45, 35, 17]
list02 = []
for item in list01:
    if item > 30:
        list02.append(item)
print(list02)