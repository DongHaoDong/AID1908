"""
    (扩展)计算一个字符串中的字符以及出现的次数
    思想
    逐一判断字符出现的次数
    如果统计过则增加1,如果没统计则等于1
"""
dict_result = {}
for item in input("请输入字符串:"):
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1
print(dict_result)

