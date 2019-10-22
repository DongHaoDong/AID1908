"""
    bool
    运算符
        比较运算符 > < >= <= == !=
        逻辑运算符 判断两个bool值关系 and(与) or(或) not(非)
"""
# bool 类型
# True(真) False(假) 取值
# 命题：带有判断性的陈述句

# 1.比较运算符
print(1 > 2)    # False
print(1 < 2)    # True
print("#####################")

# 2.逻辑运算符
# -- 与 --：一假俱假（都得满足条件，结论才成立）
print(True and False)   # False
print(False and True)   # False
print(True and True)    # True
print(False and False)  # False
print("#####################")
# -- 或 --：一真俱真（满足一个就行）
print(True or False)    # True
print(False or True)    # True
print(True or True)     # True
print(False or False)   # False
print("#####################")
# -- 非 --：取反
print(not True)         # False
print(not False)        # True




