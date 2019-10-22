"""
    元组
        基础操作
"""
# 1.创建元组

# 空
tuple01 = ()

# 具有默认值
tuple01 = (1, 2, 3)
print(tuple01)

# 列表 --> 元组
tuple01 = tuple(["a", "b"])
print(tuple01)

# 元组 --> 列表
list01 = list(tuple01)
print(list01)

# 如果元组只有一个元素
# tuple02 = 100
# print(type(tuple02))  # int
tuple02 = (100,)
print(type(tuple02))    # tuple

# 不能变化
# tuple02[0] = 10

# 2.获取元素(索引 切片)
tuple03 = ("a", "b", "c", "d")
e01 = tuple03[1]
print(type(e01))    # str
e02 = tuple03[-2:]
print(type(e02))    # tuple

# 可以直接将元组赋值多个变量
tuple04 = (100, 200)
a, b = tuple04
print(a)
print(b)

# 3.遍历元素
# 正向
for item in tuple04:
    print(item)
# 反向
# 1 0
for item in range(len(tuple04)-1, -1, -1):
    print(tuple04[item])
