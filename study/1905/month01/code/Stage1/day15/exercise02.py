"""
练习2：根据生日(年月日)，计算活了多少天
思路
年月日 --> 时间
当前时间 --> 出生时间
计算天
"""
import time
def life_days(year, month, day):
    """
        根据生日活了多少天
    :param year: 年
    :param month:月
    :param day:日
    :return: 活的天数
    """
    tuple_time = time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d")
    lift_second = time.time() - time.mktime(tuple_time)
    return int(lift_second / 60 / 60 // 24)
result = life_days(1998,4,4)
print(result)
