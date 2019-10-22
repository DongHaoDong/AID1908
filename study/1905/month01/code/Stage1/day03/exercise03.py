"""
    简易计算器
    控制台分别输入第一个数字,运算符,第二个数字
    如果控制台输入的不是 + - * / // % **则提示运算符输入有误！
"""
number01 = eval(input("请输入第一个数字:"))
operator = (input("请输入一个运算符('+_-_*_/_//_%'):"))
number02 = eval(input("请输入第二个数字:"))
if operator == "+":
    result = number01 + number02
    print("{}{}{}={}".format(number01, operator, number02, result))
elif operator == "-":
    result = number01 - number02
    print("{}{}{}={}".format(number01, operator, number02, result))
elif operator == "*":
    result = number01 * number02
    print("{}{}{}={}".format(number01, operator, number02, result))
elif operator == "/":
    result = number01 / number02
    print("{}{}{}={}".format(number01, operator, number02, result))
elif operator == "//":
    result = number01 // number02
    print("{}{}{}={}".format(number01, operator, number02, result))
elif operator == "%":
    result = number01 % number02
    print("{}{}{}={}".format(number01, operator, number02, result))
else:
    print("运算符输入错误，无法进行计算！")
