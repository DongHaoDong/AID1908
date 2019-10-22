"""
    定义函数,根据小时,分钟,秒,计算总秒数
    要求：可以只计算小时 --> 秒
         可以只计算分钟 --> 秒
         可以只计算小时+分钟 --> 秒
         可以只计算小时+秒 --> 秒
"""
def get_total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second
# 小时 + 分钟 + 秒
print(get_total_second(1, 1, 1))
# 小时 + 分钟
print(get_total_second(2, 3))
# 分钟 + 秒
print(get_total_second(minute=10, second=5))
# 小时
print(get_total_second(2))
# 分钟
print(get_total_second(minute=2))
