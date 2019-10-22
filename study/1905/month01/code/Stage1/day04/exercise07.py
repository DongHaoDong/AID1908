"""
    在控制台中获取一个整数,判断是否为素数
    素数定义：只能被1和自身整除的正数
"""
number01 = eval(input("请输入一个整数:"))
for item in range(2, number01):
    if number01 % item == 0:
        print("{}不是素数".format(number01))
        break
else:
    print("{}是素数".format(number01))

