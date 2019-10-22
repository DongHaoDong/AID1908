"""
regex.py re模块 功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"

pattern = r"(\w+):(\d+)"  # 正则表达式
# re模块直接调用findall
l = re.findall(pattern,s)
print(l)
# compile对象调用findall
regex = re.compile(pattern)
l = regex.findall(s,0,11)
print(l)
# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]',s)
print(l)
# 替换目标字符串
s = re.sub(r':','-',s,1)
print(s)
# 替换目标字符串替换几处
s = re.subn(r':','-',s,1)
print(s)
