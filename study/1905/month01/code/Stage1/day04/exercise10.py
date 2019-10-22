"""
    在控制台中重复录入一个编码值,然后打印字符
    如果输入空字符串,则退出程序
"""
while True:
    str_code = input("请输入一串编码：")
    if str_code == " ":
        break
    code_value = int(str_code)
    print(chr(code_value))
