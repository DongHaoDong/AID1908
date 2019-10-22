"""
（扩展）一个小球从100m的高度落下
    每次弹回原来高度的一半
    计算：总共弹起来多少次（最小弹起高度是0.01m）
    总共走了多少米
"""
height = 100
count = 0
distance = 0
# 弹起前高度 > 最小弹起高度
# while height > 0.01
# 弹起来的高度 > 最小弹起高度
while height / 2 > 0.01:
    # 弹起
    height /= 2
    count += 1
    print("第{}次弹起来的高度是{}米".format(count, height))
    # 累加起落高度
    distance += height * 2
print("总共弹起来{}次,总共经过的距离是{}".format(count, distance))

