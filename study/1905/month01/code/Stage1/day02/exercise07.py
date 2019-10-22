"""
    判断闰年还是平年
"""
# 闰年：年份能被4整除，但不能被100整除
year = eval(input("请输入年份："))
# if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
#     print("{}年是闰年".format(year))
# else:
#     print("{}年是平年".format(year))
result = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(result)

