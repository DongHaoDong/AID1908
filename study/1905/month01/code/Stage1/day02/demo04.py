"""
    数据类型转换
    运算符
        数学运算符
        增强运算符
"""
# 1.  数据类型转换
# int   float   str
str_usd = input("请输入美元:")
# 类型转换 str --> int
int_usd = int(str_usd)
result = int_usd * 6.9
# str + 数值 -->  str(数值)
result = str(result)
print("结果是:"+result)
# print("结果是{}".format(result))

# 2.  算数运算符
# print(1+2)
# print(1-2.5)
# 地板除（保留整数位）
print(5 // 2)   # 商2
# 余（取余）
print(5 % 2)    # 余1
# 除（取值）
print(5 / 2)    # 2.5
# 获取整数的个位
print(27 % 10)  # 7
# 幂运算
# 5的三次方
print(5**3)

# 3. 增强运算符
# number01 = 200
# print(number01 + 1)
# print(number01) # 200

number01 = 200
# 变量加上另一个数，再赋值给自身
# number01 = number01 + 1
# 累加(在自身基础上增加)
number01 += 1
print(number01)     # 201




