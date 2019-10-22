"""
一段文字中有()[]{}，编写一个接口程序去判断括号是否匹配正确
"""
from lstack import *
text = "The core (of) extensible" \
       "programming [is] defining functions." \
       "Python allows {mandatory [and]}" \
       " optional (arguments,{keyword} " \
       "arguments),and even arbitrary " \
       "argument lists."
# 将验证条件提前定义好
parens = "()[]{}"   # 特殊处理的字符集
left_parens = "([{"    # 入栈字符集
# 验证匹配关系
opposite = {"}":"{","]":"[",")":"("}
ls = LStack()   # 存储括号的栈
# 编写生成器，用来遍历字符串，不断的提供括号以及位置
def parent(text):
    # index 遍历字符串的索引位置
    index,text_len = 0,len(text)
    # 开始遍历字符串
    while True:
        while index < text_len and text[index] not in parens:
            index += 1
        # 到字符串结尾了
        if index >= text_len:
            return
        else:
            yield text[index],index
            index += 1
# 功能函数判断提供的括号是否匹配
def ver():
    for pr,index in parent(text):
        if pr in left_parens:
            ls.push((pr,index))   # 左括号入栈
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print("Unmatching is found at {} for {}".format(index,pr))
            break
    else:
        if ls.is_empty():
            print("All parentheses are matched")
        else:
            # 左括号多了
            d = ls.pop()
            print("Unmatching is found at {} for {}".format(d[1],d[0]))
# 负责逻辑验证
ver()



