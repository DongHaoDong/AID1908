"""
    练习1：从列表中[4,5,6,9,8,7]选中所有偶数
    结果存入另外一个列表中
    使用生成器实现
"""
list01 = [4,5,6,9,8,7]
def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result
result = get_even01()
for item in result:
    print(item)

def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item
g01 = get_even02()
for item in g01:
    print(item)