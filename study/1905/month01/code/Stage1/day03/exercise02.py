"""
    练习：在控制台中获取一个季节(春夏秋冬),显示相应的月份
        春 -- > 1月2月3月
        夏 -- > 4月5月6月
        秋 -- > 7月8月9月
        冬 -- > 10月11月12月
"""
season = input("请输入季节:")
if season == "春":
    print("{} -->  1月2月3月".format(season))
elif season == "夏":
    print("{} -->  4月5月6月".format(season))
elif season == "秋":
    print("{} -->  7月8月9月".format(season))
elif season == "冬":
    print("{} -->  10月11月12月".format(season))
else:
    print("输入格式不正确！")
