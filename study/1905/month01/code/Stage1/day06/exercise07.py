"""
    在控制台中循环录入学生信息(姓名,年龄,成绩,性别)
    如果名称输入为空,则停止录入
    将所有的信息逐行打印出来
"""
# 做题思路：列表内嵌字典
"""
[
    {"name":"张无忌","age":28,"score":100,"sex":男}
]
"""
list_student_info = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    age = eval(input("请输入学生年龄:"))
    score = eval(input("请输入学生成绩:"))
    sex = input("请输入学生性别:")
    dict_ifo = {"姓名": name, "年龄": age, "成绩": score, "性别": sex}
    list_student_info.append(dict_ifo)
for dict_ifo in list_student_info:
    print("{}的年龄是{}岁,成绩是{}分,性别{}".format(dict_ifo["姓名"], dict_ifo["年龄"], dict_ifo["成绩"], dict_ifo["性别"]))
# 获取第一个学生的信息
dict_ifo = list_student_info[0]
print("第一个录入的学生是{},他(她)年龄是{}岁,成绩是{}分,性别{}".format(dict_ifo["姓名"], dict_ifo["年龄"], dict_ifo["成绩"], dict_ifo["性别"]))
