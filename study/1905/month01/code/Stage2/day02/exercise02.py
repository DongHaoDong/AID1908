"""
    逆波兰表达式练习
"""

from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')    # 按空格切割
    print(tmp)
    for i in tmp:
        if i not in ['+','-','*','/','p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x-y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x*y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top())     # 查看栈顶元素
