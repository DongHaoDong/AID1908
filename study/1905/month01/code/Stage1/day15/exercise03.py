"""
    定义函数，在控制台中获取成绩的函数
    要求：如果异常，继续获取成绩，直到得到正确的成绩为止
        成绩必须在0--100之间
"""
def get_score():
    while True:
        str_result = input("请输入成绩:")
        try:
            score = int(str_result)
        except Exception:
            print("输入的不是整数")
            continue
        if 0 <=score<=100:
            return score
        else:
            print("成绩超出范围")
print(get_score())