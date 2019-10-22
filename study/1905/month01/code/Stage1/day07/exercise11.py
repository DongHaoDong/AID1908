"""
    将下列代码定义到函数中，再调用一次
"""
# 函数定义
def print_rectangle(r, c, char):
    """
    打印星星矩阵
    :param r:行数
    :param c:列数
    :param char:填充的字符
    """
    for row in range(r):
        for col in range(c):
            print(char, end=" ")
        print()
print_rectangle(5,5,"#")
