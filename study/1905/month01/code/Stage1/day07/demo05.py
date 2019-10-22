"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
for row in list01:
    for col in list02:
        list03.append(row + col)
print(list03)
list04 = [row + col for row in list01 for col in list02]
print(list04)