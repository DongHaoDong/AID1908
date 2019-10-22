"""
    （2）在控制台中购买一注彩票
    提示
        "请输入第1个红球号码:"
        "请输入第二个红球号码:"
        "号码不在范围内"
        "号码已经重复"
        "请输入蓝球号码"
"""
# 6个1 -- 33范围内的不重复红球号码
list_ticket = []
while len(list_ticket) < 6:
    number = eval(input("请输入第{}个红球号码:".format(len(list_ticket)+1)))
    if number < 0 or number > 33:
        print("号码不在范围内")
    elif number in list_ticket:
        print("号码已经重复")
    else:
        list_ticket.append(number)
# 1个1 -- 16范围内的蓝球号码
while len(list_ticket) < 7:
    number = eval(input("请输入蓝球号码:"))
    if 1 <= number <= 16:
        list_ticket.append(number)
    else:
        print("不在范围内")
print(list_ticket)
