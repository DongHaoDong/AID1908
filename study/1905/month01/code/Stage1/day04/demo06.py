"""
    通用操作  str
"""
str01 = "董浩东"
str02 = "刘凡"
# 字符串拼接
str03 = str01 + str02
print(str03)

# 字符串累加
str01 += str02
print(str01)

# 重复生成元素
print(str02 * 3)
str02 *= 3
print(str02)

# 一次比较两个容器中的元素，一旦不同则返回比较结果
print("悟空" > "八戒")

# 成员运算符
print("大圣" in "我叫齐天大圣")

# 索引
message = "我叫董浩东"
# 获取正数第三个字
print(message[2])
# 获取最后一个字
print(message[-1])

# 切片
print(message[0:2])    # 我叫
# 开始值默认为开头
print(message[:2])     # 我叫
# 结束值默认为末尾
print(message[-2:])    # 大圣
# 默认都不写取全部
print(message[:])    # 我是齐天大圣
# 大天齐
print(message[-2:-5:-1])
# 东浩董叫我
print(message[::-1])

print(message[1:1])     # 空
print(message[3:1])     # 空
print(message[-2:1])    # 空
# 索引不能越界
print(message[7])
# 切片越界不报错
print(message[1:7])



