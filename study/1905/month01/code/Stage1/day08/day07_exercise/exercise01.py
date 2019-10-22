"""
    定义在控制台打印二维列表的函数
    [
        [1,2,3,44],
        [4,5,5,5,65,6,87],
        [7,5]
    ]
    1 2 3 44
    4 5 5 5 65 6 87
    7 5
"""


def print_double_list(double_list):
    """
    打印二维列表
    :param double_list: 需要打印的二维列表
    :return:
    """
    for line in double_list:
        for item in line:
            print(item, end=" ")
        print()


list01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]
print_double_list(list01)
