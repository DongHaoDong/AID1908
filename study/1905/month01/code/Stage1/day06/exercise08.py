# 需求：存储多个学生信息(姓名,年龄,成绩,性别)
# 练习5
# 做题思路：字典内嵌列表
"""
{
    "张无忌":[28,100,"男"]
}
"""
# 练习6
# 做题思路：字典内嵌字典
"""
{
    "张无忌":{"age":28,"score":100,"sex":男}
}
"""
# 练习7
# 做题思路：列表内嵌字典
"""
[
    {"name":"张无忌","age":28,"score":100,"sex":男}
]
"""

"""
    选择策略:根据具体需求,结合优缺点,综合考虑(两害相权取其轻)
        字典：
            优点：根据key获取value,读取速度快,代码可读性相对列表更高
            缺点：内存占用大,获取值只能根据键,不灵活
        列表:
            优点：根据索引/切片,获取元素更灵活,相比字典占用内存小
            缺点：通过索引获取,如果信息较多,可读性不高
"""
# 在控制台中录入多个人的个人喜好,输入空字符串停止
"""
    请输入姓名:
        请输入第1个喜好:
        请输入第2个喜好:
        ...
    请输入姓名:
        请输入第1个喜好:
        请输入第2个喜好:
        ...
    在控制台打印所有喜好
[
    {"张无忌":[赵敏,周芷若,小昭]}
]

list_person_hobby = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    dict_person = {name: []}
    list_person_hobby.append(dict_person)
    while True:
        hobby = input("请输入喜好:")
        if hobby == "":
            break
        dict_person[name].append(hobby)
"""
"""
    {
        "张无忌":[赵敏,周芷若,小昭]
    }
"""
dict_person_hobby = {}
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    dict_person_hobby[name] = []
    while True:
        hobby = input("请输入喜好:")
        if hobby == "":
            break
        dict_person_hobby[name].append(hobby)
for name, list_hobby in dict_person_hobby.items():
    print("{}喜欢:".format(name))
    for item in list_hobby:
        print(item)
