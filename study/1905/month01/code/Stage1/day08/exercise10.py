"""
    定义函数,数值相加的函数
"""
def adds(*args):
    # result = 0
    # for item in args:
    #     result += item
    # return result
    return sum(args)
print(adds(1,2,3,4,5,6,7,8,9,10))
print(adds(1,2,3,5,6,8,10))
