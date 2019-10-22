"""
    自定义函数
"""
# 自己定义（做功能）函数
def attack():
    """
    单次攻击
    """
    print("临门一脚")
    print("直拳")
    print("摆拳")
    print("肘击")
# 形式参数
def attack_repeat(count):
    """
    重复攻击
    :param count:攻击次数,int类型
    """
    for i in range(count):
        print("临门一脚")
        print("直拳")
        print("摆拳")
        print("肘击")
# 调用函数
attack()
# .................
# 调用函数
attack()
# .................
# 调用函数
attack()
print("##########################")
# 调用函数
# 实际参数
attack_repeat(2)
