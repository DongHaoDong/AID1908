"""
    判断列表中是否存在相同的元素
"""


def is_repeating(list_target):
    """
    判断列表中是否有重复项
    :param list_target:目标列表
    :return:返回值
    """
    for row in range(0, len(list_target) - 1):
        for col in range(row + 1, len(list_target)):
            if list_target[row] == list_target[col]:
                return True
    return False


print(is_repeating([25, 26, 27, 28, 29, 30]))
