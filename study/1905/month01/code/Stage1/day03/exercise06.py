"""
    在控制台中获取一个月份
    打印天数，或者提示输入有误
    1--3--5--7--8--10--12    31
    4--6--9--11              30
    2                        28
"""
month = eval(input("请输入月份:"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("{}是31天".format(month))
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("{}是30天".format(month))
elif month == 2:
    print("{}是28天".format(month))
else:
    print("您输入的月份有误！")
