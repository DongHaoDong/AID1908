# 练习
# 在控制台中录入一个四位整数
# 计算每位相加和

# 方法一
# 控制台获取四位整数
number = eval(input("请输入一个四位整数:"))
# 个位
single_digit = number % 10
# 十位
decade = number // 10 % 10
# 百位
hundreds = number // 100 % 10
# 千位
thousands = number // 1000 % 10
# 合计
total = single_digit + decade + hundreds + thousands
print("个位数是{},十位数是{},百位数是{},千位数是{},和是{}".format(single_digit, decade, hundreds, thousands, total))

# 方法二
# 控制台获取四位整数
number = eval(input("请输入一个四位整数:"))
# 个位
result = number % 10
# 十位
result += number // 10 % 10
# 百位
result += number // 100 % 10
# 千位
result += number // 1000 % 10
print("各个位数的累加和是{}".format(result))
