"""
    循环语句
        while
"""
# 循环条件永远满足
while True:
    dollar = eval(input("请输入美元:"))
    print(dollar * 6.9)
    if input("输入q键退出:") == "q":
        break   # 退出循环体
