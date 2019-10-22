"""
    根据年月，计算有多少天？考虑闰年
"""
# 不建议方法的返回值类型可能是多种


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print(get_day_by_month(2019, 12))
