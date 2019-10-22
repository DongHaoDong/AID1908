"""
    定义方阵转置函数
"""


def square_matrix_transpose(sqr_matrix):
    """
    方阵转置
    :param sqr_matrix:二维列表类型的方阵
    :return:
    """
    for col in range(1, len(sqr_matrix)):
        for row in range(col, len(sqr_matrix)):
            sqr_matrix[row][col - 1], sqr_matrix[col - 1][row] = sqr_matrix[col - 1][row], sqr_matrix[row][col - 1]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 方阵转置的转置等于原方阵
square_matrix_transpose(list01)
print(list01)
square_matrix_transpose(list01)
print(list01)
