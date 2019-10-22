"""
# 练习2:定义生成器函数my_zip实现下列现象
# 将多个列表的每个元素与索引合成一个元组
list02 = ["孙悟空","猪八戒","唐僧","沙僧"]
list03 = [101,102,103,104]
for item in zip(list03,list02):
    print(item)
"""
# 练习2:定义生成器函数my_zip实现下列现象
# 将多个列表的每个元素与索引合成一个元组
list01 = ["孙悟空","猪八戒","唐僧","沙僧"]
list02 = [101,102,103,104]
def my_zip01(list01,list02):
    for index in range(len(list01)):
        yield (list01[index],list02[index])
for item in my_zip01(list01,list02):
    print(item)
# 扩展
def my_zip02(*args):
    # 根据星号元组形参第一个参数的长度生成索引len(args[0])
    for index in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[index])
        yield tuple(list_result)
for item in my_zip02(list01,list02):
    print(item)


