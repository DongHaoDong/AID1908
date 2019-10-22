# 使下列代码循环执行，按e键退出
while True:
    season = input("请输入:")
    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    elif season == "冬":
        print("10月11月12月")
    if input("输入e键退出:") == "e":
        break   # 退出循环体
