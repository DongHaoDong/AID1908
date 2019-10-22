"""
    ["无忌","赵敏","周芷若"]
    --> {"无忌"：2,”赵敏“:2,"周芷若":3}
"""
list01 = ["无忌", "赵敏", "周芷若"]
dict01 = {}
for item in list01:
    dict01[item] = len(item)
print(dict01)
dict02 = {item: len(item) for item in list01}
print(dict02)
