"""
    根据两计算几斤零几两
"""


def get_weight_for_jin(weight_liang):
    """
    根据两计算几斤零几两
    :param weight_liang: 需要计算的两
    :return: 元组(斤,两)
    """
    jin = weight_liang // 16
    liang = weight_liang % 16
    return (jin, liang)


weight_liang = eval(input("请输入两:"))
result = get_weight_for_jin(weight_liang)
print("{}斤{}两".format(result[0], result[1]))
