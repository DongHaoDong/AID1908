"""
    在列表[9,25,12,8]中,删除大于10的数字
"""
numbers = [9, 25, 12, 8]
for item in range(len(numbers)-1,-1,-1):
    if numbers[item] > 10:
        numbers.remove(numbers[item])
print(numbers)
