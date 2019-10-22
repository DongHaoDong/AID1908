"""
    类成员
"""
class ICBC:
    """
        工商银行
    """
    # 表示总行的钱
    total_money = 1000000
    # 因为类方法没有对象地址self,类方法不能访问实例成员
    @classmethod
    def print_total_money(cls):
        # print(id(cls),id(ICBC))
        print("总行还剩{}钱".format(ICBC.total_money))
    def __init__(self,name,money):
        self.name = name
        self.money = money
        # 表示从总行中扣除支行使用的金额
        ICBC.total_money -= money
i01 = ICBC("劳动路支行",100000)
i02 = ICBC("北大街支行",100000)
print("总行还剩{}钱".format(ICBC.total_money))
ICBC.print_total_money()
