"""
    模块相关概念
"""
# from model01 import *
# fun01()
# 隐藏成员不能通过from 模块 import * 形式导入
# _fun02()

# from model01 import _fun02
# 隐藏成员可以通过其他成员调用
# _fun02()

# 通过__all__指定可导出成员
from model01 import *
MyClass.fun03()
_fun02()

# 可以通过该属性查看文档注释
print(__doc__)
# 返回当前模块的绝对路径(从系统根目录开始的)
print(__file__)
# 现象
# 主模块叫做:__main__
# 非主模块叫：真名
print(__name__)
# 作用1：不是主模块不执行(测试代码)
# 作用 2：只有是主模块代码 才会执行(主模块代码)
# 使用
if __name__ == "__main__":
    pass

