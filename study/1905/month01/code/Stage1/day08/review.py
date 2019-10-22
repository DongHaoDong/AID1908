"""
    day07   复习
    容器
        能力提升for     for
        # 外层循环控制行
        for row in range(2):
            # 内层循环控制列
            for col in range(3):
                pass
    函数
        定义：功能,使用一个名称,包装多个语句
        语法：
            做
            def 名字(形参):
                函数体
            用
                名字(实参)
"""

#
list01 = [23, 34, 4, 6]
for row in range(len(list01) - 1):
    # 作比较
    for col in range(row + 1, len(list01)):
        if list01[row] > list01[col]:
            list01[row], list01[col] = list01[col], list01[row]
