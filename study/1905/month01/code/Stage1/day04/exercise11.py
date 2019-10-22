"""
    在控制台中获取一个字符串
    打印第一个字符
    打印最后一个字符
    打印倒数第三个字符
    打印前两个字符
    倒序打印字符
    如果字符串长度是奇数,则打印中间字符
"""
str01 = input("请输入一个字符串:")
print(str01[0])
print(str01[-1])
print(str01[-3])
print(str01[:2])
print(str01[::-1])
if len(str01) % 2 == 1:
    print(str01[len(str01) // 2])
