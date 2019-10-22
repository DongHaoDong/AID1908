"""
    在控制台中获取月份,显示季度，或者提示月份输入不对
"""
while True:
    month = input("请输入月份:")
    if month == "1" or month == "2" or month == "3":
        print("{}月是第一季度".format(month))
    elif month == "4" or month == "5" or month == "6":
        print("{}月是第二季度".format(month))
    elif month == "7" or month == "8" or month == "9":
        print("{}月是第三季度".format(month))
    elif month == "10" or month == "11" or month == "12":
        print("{}月是第四季度".format(month))
    else:
        print("月份输入不正确！")
