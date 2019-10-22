"""
    真值表达式
        if 数据：
            语句
        本质上是使用bool函数操作数据
    条件表达式

"""
# 1.真值表达式
# if 100:
#     print("真值")
# str_input = input("请输入:")
# if str_input:
#     print("输入的字符串不是空的")

# 条件表达式
sex = None
if input("请输入性别:") == "男":
    sex = 1
else:
    sex = 0
print(sex)

sex = 1 if input("请输入性别：") == "男 " else 0
print(sex)
