"""
    str 字面值
    转义符：改变原始字符含义的符号
"""
name = "董浩东"
name = '董浩东'

# 所见即所得
name = '''董浩东'''
name = """
        董
            浩
                东
"""
print(name)

# 单引号内的双引号不算结束符
message = '我叫"董浩东"。'

# 双引号内的单引号不算结束符
message = "我叫'董浩东'。"

# 转义符 \ \t \n
message = "我叫\"董浩东\"。"
message = "我叫\n董浩东。"
message = "我叫\t董浩东。"

# 利用转义符将\进行转义
url = "F:\\python\\dist"

# 原始字符串：取消转义
url = r"F:\python\dist"
print(url)

# 字符串格式化
a = 1
b = 2
# "请输入" + str(a) + "+" +str(b) + "=?"
# 在字符串中插入变量
# 请输入1+2=？
str01 = "请输入%d+%d=?" % (a, b)
print(str01)
