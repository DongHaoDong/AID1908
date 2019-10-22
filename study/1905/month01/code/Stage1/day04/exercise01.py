"""
    在控制台中获取一个开始值,一个结束值
    将两个数中间的数打印出来
"""
Start = eval(input("请输入开始值:"))
End = eval(input("请输入结束值："))
while Start < End - 1:
    print(Start + 1, end=" ")
    Start += 1
