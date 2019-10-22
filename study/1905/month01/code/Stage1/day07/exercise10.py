"""
    列表全排列
    ["香蕉", "苹果", "哈密瓜"]
    ["可乐","牛奶"]
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["可乐", "牛奶"]
list03 = []
for row in list01:
    for col in list02:
        list03.append(row + col)
list04 = [row + col for row in list01 for col in list02]
print(list03)
print(list04)
