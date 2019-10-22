"""
    字典
"""
# 1.创建字典
# 空
dict01 = {}
dict01 = dict()
# 默认值
dict01 = {"wj": 100, "zm": 80, "zr": 90}
dict01 = dict([("a", "b"), ("c", "d")])
print(dict01)
# 2.查找元素(根据key查找value)
print(dict01["a"])
# 如果键不存在，查找是会报错
# 如果存在键
if "aa" in dict01:
    print(dict01["aa"])
# 3.修改元素(键存在修改)
dict01["a"] = "BB"
print(dict01["a"])
# 4.添加(键不存在添加)
dict01["e"] = "f"
print(dict01)
# 5.删除
del dict01["a"]
print(dict01)
# 6.遍历
# 遍历字典,得到的是key
for key in dict01:
    print(dict01[key])
# 遍历字典,获取value
for value in dict01.values():
    print(value)
# 遍历字典,获取键值对key value
for item in dict01.items():
    print(item)
# 分别拿出键和值
for k, v in dict01.items():
    print(k)
    print(v)


