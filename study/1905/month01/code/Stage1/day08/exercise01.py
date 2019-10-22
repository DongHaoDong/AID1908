"""
    计算整数的每位相加和
"""


def each_unit_sum(number):
    """
    计算整数的每位相加和
    :param number: 四位整数
    :return: 相加的结果
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000 % 10
    return result


result01 = each_unit_sum(1234)
print("结果是{}".format(result01))
result01 = each_unit_sum(1234)
print("结果是{}".format(result01))
