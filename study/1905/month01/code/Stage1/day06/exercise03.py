"""
    练习：在控制台录入日期（月日）,计算这是一年的第几天
    例如：3月5日
        1月天数+2月天数+5月天数
"""
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = eval(input("请输入月份:"))
day = eval(input("请输入日期:"))
# 方法一：
# 累加前几个月的天数
# total_day = 0
# for item in range(month-1):
#     total_day += day_of_month[item]
# # 累加当月的天数
# total_day += day
# print("{}月{}日是一年的第{}天".format(month, day, total_day))

# 方法二：
total_day = sum(day_of_month[:month-1])
total_day += day
print("{}月{}日是一年的第{}天".format(month, day, total_day))