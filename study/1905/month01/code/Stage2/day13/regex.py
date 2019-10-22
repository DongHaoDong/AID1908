"""
regex.py
match 对象演示
"""
import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefghi',0,8) # match对象
# 属性变量
print(obj.pos)  # 目标字符串的开始位置
print(obj.endpos)   # 目标字符串的结束位置
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)    # 最后一组组名
print(obj.lastindex)    # 最后一组序号
print("===============================")
# 属性方法
print(obj.span())   # 匹配内容在字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 生成捕获组字典
print(obj.groups())  # 子组对应内容元组
print(obj.group(1))  # 获取match对应的内容





