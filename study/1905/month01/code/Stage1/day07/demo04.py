"""
    for for
"""
# 外层循环控制行
for row in range(4):
    # 内层循环控制列
    for col in range(5):
        print("*", end=" ")
    print()
"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""
# 外层循环控制行
for row in range(4):
    # 内层循环控制列
    for col in range(6):
        if col % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
"""
    *
    **
    ***
    ****
"""
for row in range(4):
    for col in range(row + 1):
        print("*", end="")
    print()
