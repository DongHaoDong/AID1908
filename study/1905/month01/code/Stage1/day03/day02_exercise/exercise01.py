"""
    已知：加速度，初速度，时间
        计算：距离
        加速度 = （距离 - 初速度 × 时间） × 2 / 时间平方
"""
# 1. 距离 = 加速度 × 时间平方 / 2 + 初速度 × 时间
acceleration_speed = eval(input("请输入加速度:"))
initial_speed = eval(input("请输入初速度:"))
time = eval(input("请输入时间:"))
distance = (acceleration_speed * pow(time, 2) / 2 + initial_speed * time )
print("距离是{}".format(distance))
