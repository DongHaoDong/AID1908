"""
    定义列表升序排列的函数
"""


def sort(list_target):
    # 满足以下两个条件,就无需通过返回值传递结果
    # 1.传入的是可变对象
    # 2.函数体修改的是传入的对象
    for row in range(len(list_target) - 1):
        # 作比较
        for col in range(row + 1, len(list_target)):
            if list_target[row] > list_target[col]:
                list_target[row], list_target[col] = list_target[col], list_target[row]


list01 = [2, 6, 9, 8, 744, 55, 33, 22]
sort(list01)
print(list01)
