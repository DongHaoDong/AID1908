"""
    在控制台中录入一个成绩,判断等级（优秀/良好/中等/及格/不及格/输入有误）
"""
score = eval(input("请输入您的成绩:"))
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 70 <= score < 80:
    print("中等")
elif 60 <= score < 70:
    print("良好")
elif 0 <= score < 60:
    print("不及格")
else:
    print("输入格式不对")