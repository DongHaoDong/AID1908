"""
    2048游戏核心算法
"""
list_merge = None
# 1.练习1零元素移至末尾
#  [2,0,2,0] --> [2,2,0,0,]
#  [2,0,0,2] --> [2,2,0,0,]
#  [2,4,0,2] --> [2,4,2,0,]


def zero_to_end():
    """
        零元素移动到末尾
    :return:
    """
    # 从后向前,如果发现0元素删除,并在末尾追加
    for index in range(-1, -len(list_merge)-1, -1):
        if list_merge[index] == 0:
            del list_merge[index]
            list_merge.append(0)


# 测试代码
# zero_to_end()
# print(list_merge)

# 练习2：将相同数字进行合并
#  [2,2,0,0] --> [2,0,0,0,]
#  [2,0,0,2] --> [2,0,0,0,]
#  [2,0,4,0] --> [2,4,0,0,]
#  [2,2,2,2] --> [4,4,0,0,]
#  [2,2,2,0] --> [4,2,0,0,]


def merge():
    """
        合并
    """
    # 先将中间的零元素移至末尾
    # 再合并相邻相同元素
    for index in range(len(list_merge)-1):
        zero_to_end()
        if list_merge[index] == list_merge[index+1]:
            # 后一个累加前一个之上
            list_merge[index] += list_merge[index+1]
            del list_merge[index+1]
            list_merge.append(0)


# 测试
# merge()
# print(list_merge)


# 练习3：地图向左移动
map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2],
]


def move_left():
    """
        向左移动
    :return:
    """
    # 将二维列表中每行交给merge函数进行操作
    for line in map:
        global list_merge
        list_merge = line
        merge()


# 测试
# move_left()
# print(map)


def move_right():
    """
        向右移动
    :return:
    """
    # 思想：将二维列表中每行从优向左交给merge函数进行操作

    for line in map:
        global list_merge
        # 从优向左取出数据形成新列表
        list_merge = line[::-1]
        merge()
        # 从右向左 接收合并后的数据
        line[::-1] = list_merge

# 测试
# move_right()
# print(map)


# 练习4：向上移动  向下移动
def move_up():
    """
        向上移动
    :return:
    """
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


def move_down():
    """
        向下移动
    :return:
    """
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)

# 提示利用方阵转置函数
def square_matrix_transpose(sqr_matrix):
    """
    方阵转置
    :param sqr_matrix:二维列表类型的方阵
    :return:
    """
    for col in range(1, len(sqr_matrix)):
        for row in range(col, len(sqr_matrix)):
            sqr_matrix[row][col - 1], sqr_matrix[col - 1][row] = sqr_matrix[col - 1][row], sqr_matrix[row][col - 1]


move_down()
print(map)


