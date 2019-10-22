"""
    在控制台中循环输入字符串,如果输入空则停止
"""
str01 = []
while True:
    str01_input = input("请输入一个字符串:")
    if str01_input == "":
        break
    str01.append(str01_input)
result = "*".join(str01)
print(result)