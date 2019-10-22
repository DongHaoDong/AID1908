"""
4.(扩展)方阵转置
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for col in range(1, len(list01)):
    for row in range(col, len(list01)):
        list01[row][col-1], list01[col-1][row] = list01[col-1][row], list01[row][col-1]