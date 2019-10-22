"""
    猜数字游戏2.0
    电脑随机生成一个数字
    然后用户输入一个数字进行猜测
    如果猜对了程序退出,并输出猜了多少次
"""
import random
computer = random.randint(1, 100)
count = 0
while count < 3:
    player = eval(input("请输入一个数字:"))
    count += 1
    if player > computer:
        print("猜大了")
    elif player < computer:
        print("猜小了")
    elif player == computer:
        print("恭喜你,猜对了,您猜了{}次".format(count))
        break   # 退出 循环体，不会执行else
else:
    print("游戏结束")
