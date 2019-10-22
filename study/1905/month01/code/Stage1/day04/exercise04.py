"""
    根据成绩判断等级,如果录入空字符串,程序退出
    如果录入成绩错误达到3次，则退出程序并显示成绩输入错误
"""
count = 0
while count < 3:
    str_score = input("请输入一个成绩:")
    if str(str_score) == "":
        break
    score = int(str_score)
    if 90 <= score <= 100:
        print("优秀")
    elif 80 <= score < 90:
        print("良好")
    elif 70 <= score < 80:
        print("中等")
    elif 60 <= score < 70:
        print("及格")
    elif 0 <= score < 60:
        print("不及格")
    elif score > 100 or score <0:
        print("录入错误")
        count += 1
else:
    print("输入次数过多,程序结束！")
