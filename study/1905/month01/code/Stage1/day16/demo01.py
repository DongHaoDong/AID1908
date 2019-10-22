"""
    可迭代对象
"""
# 可迭代对象   --容器
list01 = [43,45,25,78,956]
# 迭代过程
# for item in list01:
#     print(item)

# 迭代原理
# 面试题：for循环的原理是什么？
#        答：1、获取迭代器
#            2、循环获取下一个元素
#            3、遇到异常停止迭代
#         可以被for的条件是什么?
#        答：能被for的对象必须具备__iter__方法
#        答：能被for的对象必须是可迭代对象
# 1.获取迭代器
iterator = list01.__iter__()
# 2.循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
# 3.遇到异常 停止迭代
    except StopIteration:
        break   # 退出循环