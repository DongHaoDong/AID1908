"""
    在控制台中录入所有学生姓名
    如果姓名重复，则提示姓名已经存在,不能添加到列表中
    输入空格,倒叙打印所有学生
"""
names = []
while True:
    name = input("请输入学生姓名:")
    if name == "":
        break
    # 判断变量在列表中是否存在
    if name not in names:
        names.append(name)
    else:
        print("姓名已经存在，不能添加到列表中")
for index in range(-1, -len(names)-1, -1):
    print(names[index])




