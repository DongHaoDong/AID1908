"""
    装饰器
"""
"""
# 需求:对以下两个功能增加权限验证

# 需要增加的功能
def verify_permission():
    print("权限验证")
# 已有功能
def enter_background():
    verify_permission()
    print("进入后台")
def delete_order():
    verify_permission()
    print("删除订单")
enter_background()
delete_order()
# 缺点：增加新功能，需要修改已有功能 [违反开闭原则]
"""
"""
# 需要添加的功能
def verify_permission(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper
# 已有功能
def enter_background():
    print("进入后台")
def delete_order():
    print("删除订单")
# enter_background = 新功能 + 旧功能
enter_background = verify_permission(enter_background)
delete_order = verify_permission(delete_order)

enter_background()
delete_order()
# 缺点：每次拦截对已有功能(enter_background)的调用,不科学
"""
"""
# 需要添加的功能
def verify_permission(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper
# 已有功能
# enter_background = verify_permission(enter_background)
@verify_permission
def enter_background():
    print("进入后台")
# delete_order = verify_permission(delete_order)
@verify_permission
def delete_order():
    print("删除订单")


enter_background()
delete_order()
# 缺点：如果已有功能参数不统一，无法进行包装
"""
# 需要添加的功能
def verify_permission(func):
    def wrapper(*args,**kwargs):
        print("权限验证")
        func(*args,**kwargs)
    return wrapper
# 已有功能
@verify_permission
def enter_background(login_id,pwd):
    print(login_id,pwd,"进入后台")
@verify_permission
def delete_order(order_id):
    print("删除订单",order_id)


enter_background("dream",1234)
delete_order(101)