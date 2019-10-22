"""
    复习
    函数式编程
        函数作为参数
            自定义高阶函数list_helper.py
            内置高阶函数
                map(函数,可迭代对象) --> ListHelper.select(可迭代对象，函数)
                filter(函数,可迭代对象) --> ListHelper.find_all(可迭代对象,函数)
                max(可迭代对象,key = 函数) --> ListHelper.get_max(可迭代对象,函数)
                min(可迭代对象,key = 函数) -->
                sorted(可迭代对象,key = 函数) --> ListHelper.order_by(可迭代对象,order_by)
                sorted(可迭代对象,key = 函数,reverse = True) 降 --> ListHelper.order_by(可迭代对象,order_by)
        函数作为返回值

"""