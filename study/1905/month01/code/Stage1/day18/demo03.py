"""
    闭包
"""
def fun01():
    a = 1
    def fun02():
        print(a)
    return fun02
# 调用外部函数，返回值是内嵌函数
result = fun01()
# 调用内嵌函数
result()    # 可以访问外部变量a

# 闭包应用
# 压岁钱
def give_gife_money(money):
    """
        得到压岁钱
    :return:
    """
    print("得到了{}压岁钱".format(money))
    def child_buy(target,price):
        """
            孩子购买商品
        :param target:需要购买的商品
        :param price:商品单价
        """
        nonlocal money
        if money >= price:
            money -= price
            print("孩子花了{}钱,购买了{}".format(price,target))
        else:
            print("钱不够了")
    return child_buy
# 下列代码是一个连续的逻辑
action = give_gife_money(10000)
action("唐僧肉",0.5)
action("小汽车",2000)
action("手机",8000)