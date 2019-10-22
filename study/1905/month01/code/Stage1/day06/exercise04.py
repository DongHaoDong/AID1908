"""
    练习1：在商品中循环录入商品信息（名称,单价）
        如果名称输入为空,则停止录入
        将所有的信息逐行打印出来
"""
dict_goods = {}
while True:
    good = input("请输入商品名称:")
    if good == "":
        break
    else:
        price = eval(input("请输入商品单价："))
        dict_goods[good] = price
for item in dict_goods.items():
    print(item)
