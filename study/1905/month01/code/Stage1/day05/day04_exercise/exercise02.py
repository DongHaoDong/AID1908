"""
    4. 在控制台获取一个整数作为边长
    根据边长打印矩形
    例如：4
        ****
        *  *
        *  *
        ****
"""
number = eval(input("请输入一个整数:"))
if number <= 1:
    print("输入的数字必须大于1")
else:
    print("*" * number)
    for item in range(number - 2):
        print("*" + " " * (number - 2) + "*")
    print("*" * number)
