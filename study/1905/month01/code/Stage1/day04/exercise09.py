"""
    在控制台中获取一个字符串打印每个字符的编码值
"""
str01 = input("请输入你要转换编码的文本:")
for item in str01:
    print(ord(item), end=" ")
