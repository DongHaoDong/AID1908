"""
    在控制台中循环录入学生信息(姓名,年龄,成绩,性别)
    如果名称输入为空,则停止录入
    将所有的信息逐行打印出来
"""
# 做题思路：字典内嵌字典
"""
{
    "张无忌":{"age":28,"score":100,"sex":男}
}
"""
dict_student_info = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = eval(input("请输入学生年龄:"))
    score = eval(input("请输入学生成绩:"))
    sex = input("请输入学生性别:")
    dict_student_info[name] = {"年龄": age, "成绩": score, "性别": sex}
for name, dict_ifo in dict_student_info.items():
    print("{}的年龄是{}岁,成绩是{}分,性别{}".format(name, dict_ifo["年龄"], dict_ifo["成绩"], dict_ifo["性别"]))
