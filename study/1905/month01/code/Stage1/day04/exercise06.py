"""
    随机加法考试
        随机产生两个数字（1-10）
        在控制台中获取两个数相加的结果
        如果用户输入正确得10分
        总共3道题，最后输出得分
"""
import random
score = 0
for item in range(3):
    number01 = str(random.randint(1, 10))
    number02 = str(random.randint(1, 10))
    result = input("请输入{}+{}的结果:".format(number01,number02))
    if result == str(int(number01) + int(number02)):
        score += 10
print("您的成绩是{}分".format(score))
