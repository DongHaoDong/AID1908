"""
    （扩展）在控制台中获取总秒数，计算几小时积分零几秒
"""
total_second = eval(input("请输入总秒数:"))
# 商：分钟数     余数：零几秒
second = total_second % 60
# 分钟：总秒数 / 60 取商表示总分钟数
#      总分钟数 / 60 取商表示总小时
hour = total_second // 60 // 60
# 分钟：总秒数 / 60 取商表示总分钟数
#      总分钟 / 60 取余表示总小时剩下的分钟数
minute = total_second // 60 % 60
print("{}小{}分{}秒".format(hour, minute,second))
