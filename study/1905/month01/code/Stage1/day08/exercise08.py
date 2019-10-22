"""
    统计一个函数的执行次数
"""

count = 0
def fun01():
    global count
    count += 1

fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print("函数调用了{}次".format(count))


