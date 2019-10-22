"""
    在控制台中录入一个字符串，判断是否为回文
    判断规则：
    正向与反向相同
    上海自来水来自海上
"""
message = input("请输入一段字符串")
if message == message[::-1]:
    print("您输入的是回文！")
else:
    print("您输入的不是回文!")
