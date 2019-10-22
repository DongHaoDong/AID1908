"""
    列表排序（升序）[3,80,45,5,7,1]
"""
list01 = [3, 80, 45, 5, 7, 1]
# for row in range(len(list01)-1):
#     for col in range(len(list01)-row-1):
#         if list01[col] > list01[col+1]:
#             list01[col], list01[col+1] = list01[col+1], list01[col]
# print(list01)
for row in range(len(list01)-1):
    for col in range(row+1, len(list01)):
        if list01[row] > list01[col]:
            list01[row], list01[col] = list01[col], list01[row]
print(list01)
