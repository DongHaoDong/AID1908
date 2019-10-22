"""
    在控制台中循环录入学生信息(姓名,年龄,成绩,性别)
    如果名称输入为空,则停止录入
    将所有的信息逐行打印出来
"""
# 做题思路：字典内嵌列表
dict_student = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = eval(input("请输入学生年龄:"))
    score = eval(input("请输入学生成绩:"))
    sex = input("请输入学生性别:")
    dict_student[name] = [age, score, sex]
for name, list_ifo in dict_student.items():
    print("{}的年龄是{}岁,成绩是{}分,性别{}".format(name, list_ifo[0], list_ifo[1], list_ifo[2]))
