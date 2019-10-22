"""
    在控制台中循环录入字符串,输入空字符串停止
    打印所有不重复的文字
"""
str_set = set()
while True:
    str_input = input("请输入字符串：")
    if str_input == "":
        break
    str_set.add(str_input)
print(str_set)
