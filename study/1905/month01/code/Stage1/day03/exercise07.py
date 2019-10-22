"""
    在控制台中获取一个整数
    如果是偶数为变量state赋值"偶数"，否则赋值"奇数"
    在控制台录入一个年份
    如果是闰年，给变量day赋值29,否则赋值28
"""

# 在控制台中获取一个整数
# 如果是偶数为变量state赋值"偶数"，否则赋值"奇数"
number01 = eval(input("请输入一个整数:"))
# if number01 % 2 == 0:
#     state = "偶数"
# else:
#     state = "奇数"
state = "奇数" if number01 % 2 else "偶数"
print("{}".format(state))

# 在控制台录入一个年份
# 如果是闰年，给变量day赋值29,否则赋值28
year = eval(input("请输入年份"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     day = 29
# else:
#     day = 28

# 代码可读性 很差
# if not year % 4 and year % 100 or not year % 400:
#     day = 29
# else:
#     day = 28
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print("{}".format(day))

