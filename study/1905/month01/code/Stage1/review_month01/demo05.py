# 解释器会将方法定义到方法区(存储一份),连同默认参数一起创建
# 所以不指定参数时，使用的就是那一份列表对象
# 总结，默认参数，不要使用可变对象
def fun01(x,list_target = []):
    print(id(list_target))
    for index in range(x):
        list_target.append(index)
    print(list_target)
fun01(3)    # [0,1,2]
fun01(3)    # [0,1,2,0,1,2]
list01 = []
fun01(3,list01)