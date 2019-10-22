"""
    3.  按照以下格式输出变量name = "孙悟空",age = 800,score =  98
        我叫xxx,年龄是xxx,成绩是xxx
"""
name = "孙悟空"
age = 800
score = 99.5
message = "我叫{},年龄是{},成绩是{}".format(name, age, score)
message = "我叫%s,年龄是%d,成绩是%.1f" % (name, age, score)
print(message)
