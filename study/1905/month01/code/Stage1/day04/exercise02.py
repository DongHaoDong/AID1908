"""
    一张纸的厚度是0.01mm
    对折多少次厚度能超过珠穆朗玛峰（8844.43米）
"""
thickness = 0.01 / 1000
count = 0
while thickness <= 8848.43:
    thickness *= 2
    count += 1
    # print(thickness)
print("一张纸对折{}次能超过珠穆朗玛峰".format(count))
