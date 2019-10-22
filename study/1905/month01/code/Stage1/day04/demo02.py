"""
    for：    适合执行指定次数
    while:   适合根据条件循环执行
"""
# for 变量列表 in 可迭代对象:
#     语句块1
# else:
#     语句块2
str01 = "我叫董浩东!"
for item in str01:
    print(item, end=" ")

# 整数生成器： rang(开始,结束,步长)
# for + range：更擅长执行预定次数
for item in range(5):
    print(item, end=" ")

# 需求：一张纸对折10次
thickness = 0.0001
for item in range(10):
    thickness *= 2
print(thickness)
