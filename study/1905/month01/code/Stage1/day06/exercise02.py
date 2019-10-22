"""
    借助元组完成下列功能
"""
# 方式1：
# month = eval(input("请输入月份:"))
# if month not in tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
#     print("输入有误")
# elif month in (2,):
#     print("28天")
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     print("31天")
# elif month in (4, 6, 9, 11):
#     print("30天")

# 方式2
month = eval(input("请输入月份:"))
if month not in tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    print("输入有误")
else:
    # 将每月天数存入元组
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_of_month[month-1])




