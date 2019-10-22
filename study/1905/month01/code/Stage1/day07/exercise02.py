"""
    ["无忌","赵敏","周芷若"]   [101,102,103]
    {"无忌":101,"赵敏":102,"周芷若":103}
"""
list01 = ["无忌", "赵敏", "周芷若"]
list02 = [101, 102, 103]
dict01 = {}
# 通过索引同时在多个列表中获取元素
for index in range(len(list01)):
    dict01[list01[index]] = list02[index]
print(dict01)
dict02 = {list01[index]: list02[index] for index in range(len(list01))}
print(dict02)
# 字典如何根据value查找键
# 解决方案1   键值互换
dict03 = {value: key for key, value in dict01.items()}
print(dict03)
print(dict03[101])
# 缺点:如果key重复,交换则丢失数据
# 如果需要保持所有数据
# [(k,v),]
list02 = [(key, value) for key, value in dict01.items()]
print(list02)
