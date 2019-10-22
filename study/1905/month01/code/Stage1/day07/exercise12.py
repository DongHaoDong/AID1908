"""
    在控制台中打印一维列表的函数
    例如[1,2,3]-->1 2 3   每个元素一行
"""
def print_list(list_target):
    """
    打印列表
    :param list_target: 目标列表
    """
    for item in list_target:
        print(item)
list01 = [1, 2, 3]
list02 = [4, 5, 6]
print_list(list02)