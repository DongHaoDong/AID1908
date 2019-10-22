"""
    定义函数,计算指定范围内的素数
    备注:没有判断2以下的数字
"""


# def get_prime(begin, end):
#     list01_result = []
#     # 生成一定范围内的数字
#     for number in range(begin, end):
#         # 判断素数
#         for item in range(2, number):
#             if number % item == 0:
#                 break
#         else:
#             list01_result.append(number)
#     return list01_result
#
#
# print(get_prime(5, 30))


def is_prime(number):
    """
    判断指定数字是否是素数
    :param number: 指定的整数
    :return: True 是素数,False不是素数
    """
    for item in range(2, number):
        if number % item == 0:
            return False
    return False


def get_prime(begin, end):
    """
    获取指定范围内的素数
    :param begin: 开始值(包含)
    :param end: 结束值(不包含)
    :return: 返回素数列表
    """
    list01_result = []
    for number in range(begin, end):
        if is_prime(number):
            list01_result.append(number)
    return list01_result


print(get_prime(5, 30))
