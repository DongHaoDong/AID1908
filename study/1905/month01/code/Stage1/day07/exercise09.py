"""
    矩阵转置    将二维列表的列变成行
    第一列变成第一行
    第二列变成第二行
    第三列变成第三行
"""
# 00 10 20 30
list01 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
# result = []
# for col in range(4):
#     line = []
#     result.append(line)
#     for row in range(4):
#         line.append(list01[row][col])
result = []
for col in range(len(list01[0])):
    result.append([])
    for row in range(len(list01)):
        result[col].append(list01[row][col])
print(result)
