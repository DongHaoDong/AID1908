# 练习
# 在控制台中,录入一个商品单价25
# 再录入一个数量2
# 最后获取应收金额,计算应该找回多少钱
price = eval(input("请输入商品单价:"))
num = eval(input("请输入您要购买商品的数量:"))
Amount = price * num
print("您应付{}元".format(Amount))
money = eval(input("请支付的金额:"))
balance = money - Amount
print("找您{}元".format(balance))
print('''
    您的消费详情如下
    ×××××××××××××××××
    商品单价    {}元
    购买数量    {}个
    合计       {}元
    应付       {}元
    实付       {}元
    找零       {}元
    ××××××××××××××××
'''.format(price,num,Amount,Amount,money,balance))



