"""
    del 语句
"""
a = "悟空"
b = a
c = a
# 删除变量a,b,不释放对象"悟空"
del a, b
# 由于变量C不再引用对象"悟空",而悟空的引用计数为0，所以被标记为可回收
C = None
