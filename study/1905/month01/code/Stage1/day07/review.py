"""
    day06   复习
    容器
        字符串：不可变     存储编码值      序列
        列表：可变       存储变量        序列
            预留空间
            扩容：开辟更大的空间  拷贝原有数据  替换引用
        元组：不可变      存储变量        序列
            按需分配
        字典：可变   存储键值对   散列
"""
list01 = []
list01 = ["dhd", "bb", "mdl"]
list01.append("zzm")
list01.insert(1, "lf")
# 指向列表中的元素
for item in list01:
    print(item)
# 变量 index 表示索引
for index in range(len(list01)):
    print(list01[index])
# 修改
list01[0] = "DHD"

# 删除
list01.remove("mdl")

dict01 = {"dhd": 100, "bb": 95, "mdl": 90}
dict01["zzm"] = 85
# 获取字典中的所有元素
# 获取字典中的键
for key in dict01:
    print(key)
# 获取字典中的值
for value in dict01.values():
    print(value)
# 获取字典中的键值对
for item in dict01.items():
    print(item)
# 分别获取字典中的键的集合和值的集合
for key, value in dict01.items():
    print(key)
    print(value)
# 修改
dict01["qtx"] = 101

# 删除
del dict01["mdl"]
list02 = ["看书", "学习", "编程"]
dict02 = {"dhd": list02}
list02.append("听音乐")
print(dict02)
