"""
    在控制台录入五个数字
    然后输出最大值
"""
# 假设的最大值
max_value = 0
for item in range(5):
    number = eval(input("请输入第{}个数字:".format(item+1)))
    if max_value < number:
        max_value = number
print(max_value)

