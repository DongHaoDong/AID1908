# 在控制台中录入距离,时间,初速度,计算加速度
# 匀变速直线运动的位移与时间公式:
# 加速度 = （距离 - 初速度 × 时间）× 2 / 时间平方
distance = eval(input("请输入距离:"))
time = eval(input("请输入时间:"))
initial_speed = eval(input("请输入初速度"))
acceleration_speed = ((distance - initial_speed * time) * 2) / (pow(time, 2))
print("加速度是{}".format(acceleration_speed))