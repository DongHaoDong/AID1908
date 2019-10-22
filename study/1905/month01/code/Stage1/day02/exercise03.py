# 练习2：在控制台中获取分钟
#       再获取小时
#       再获取天
#       计算总秒数
minute = eval(input("请输入分钟:"))
hour = eval(input("请输入小时:"))
day = eval(input("请输入天:"))
result = minute * 60 + hour * 3600 + day * 86400
print("总秒数是{}秒".format(result))
