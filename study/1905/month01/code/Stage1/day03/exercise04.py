"""
    控制台分别录入4个数字
    打印最大的数字
"""
number01 = eval(input("请输入第1个数字:"))
number02 = eval(input("请输入第2个数字:"))
number03 = eval(input("请输入第3个数字:"))
number04 = eval(input("请输入第4个数字:"))
max_value = number01
if max_value < number02:
    max_value = number02
if max_value < number03:
    max_value = number03
if max_value < number04:
    max_value = number04
print(max_value)