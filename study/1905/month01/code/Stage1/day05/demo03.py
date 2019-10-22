"""
    str list
"""
# 需求：根据xx逻辑,拼接一个字符串
# "0123456789"
# 每次循环形成新字符串对象,替换变量引用result= ""
# result = ""
# for item in range(10):
#     result += str(item)
# print(result)
# 每次循环只向列表中添加字符串,没有创建列表对象
list_temp = []
for item in range(10):
    list_temp.append(str(item))
    # 把一个列表变成字符串
    result = "\t".join(list_temp)
print(result)
