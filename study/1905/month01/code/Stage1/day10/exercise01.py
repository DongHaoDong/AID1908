"""
[
    {
        "name":name,
        "age":age,
        "score":score,
        "sex":sex,
    }
]
# 练习
1.创建学生类
    --数据:姓名，年龄，成绩，性别
    --行为:在控制台中打印个人信息的方法
2.在控制台中循环录入学生信息，如果名称是空字符串，退出录入
3.控制台中输出每个人的学生信息（调用打印学生类的打印方法）
4.打印第一个学生的信息
"""
# list_student_info = []
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))
#     dict_info = {"name": name, "age": age, "score": score}
#     list_student_info.append(dict_info)
# for dict_info in list_student_info:
#     print("{}的年龄是{},成绩是{},性别是{}".format(dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
#     dict_info = list_student_info[0]
#     print("第一个录入的是:{},年龄是{},成绩是{},性别是{}".format(dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
list_student_info = []
class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex
    def print_self_info(self):
        print("{}的年龄是{},成绩是{},性别是{}".format(self.name, self.age, self.score, self.sex))
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    student = Student(name,age,score,sex)
    list_student_info.append(student)
for student in list_student_info:
    student.print_self_info()
# 获取第一个学生信息
info = list_student_info[0]
info.print_self_info()




