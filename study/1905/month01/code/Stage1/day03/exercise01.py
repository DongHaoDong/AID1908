"""
    当钱不够时,提示"金额不足"
    钱足够时,提示"应找回"
    调试程序
"""
price = eval(input("请输入商品单价:"))
count = eval(input("请输入商品数量:"))
money = eval(input("请输入金额:"))
amount = price * count
if money > amount:
    surplus = money - amount
    print("应付{}元,您支付了{}元,找零{}元".format(amount, money, surplus))
elif money == amount:
    surplus = money - amount
    print("应付{}元,您支付了{}元,找零{}元".format(amount, money, surplus))
else:
    surplus = money - amount
    print("应付{}元,您支付了{}元,金额不足,还差{}".format(amount, money, abs(surplus)))