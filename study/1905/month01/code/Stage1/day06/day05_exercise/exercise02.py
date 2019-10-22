"""
    彩票  双色球
    红球：6个,1 -- 33 之间的整数 不能重复
    蓝球：1个,1 -- 16 之间的整数
    （1）随机产生一注彩票[6个红球1个蓝球]
"""
import random
list_ticket = []
# 6个不重复的红球
while len(list_ticket) < 6:
    random_number = random.randrange(1, 33)
    # 如果随机数不存在则存储
    if random_number not in list_ticket:
        list_ticket.append(random_number)
# 一个随机的蓝球
list_ticket.append(random.randrange(1, 16))
print(list_ticket)
