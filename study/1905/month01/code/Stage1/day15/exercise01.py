"""
    练习1：定义函数，根据年与日，返回星期数。
        "星期一"
        "星期二"
        "星期三"
        "星期四"
        "星期五"
        ...
        思路：年月日 --> 时间元组
        时间元组 --> 星期
        星期 --> 格式
"""
import time
def get_week(year,month,day):
    """
        获取星期几
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 星期几
    """
    tuple_time = time.strptime("{}-{}-{}".format(year,month,day), "%Y-%m-%d")
    dict_weeks = {
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",
        6:"星期日",
    }
    return dict_weeks[tuple_time[6]]
result = get_week(2019,10,1)
print(result)



