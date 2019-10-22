"""
    温度转换器
        摄氏度 = （华氏度 - 32）/ 1.8
        华氏度 = 摄氏度 × 1.8 + 32
        开氏度 = 摄氏度 + 273.15
        （1）获取华氏度，计算摄氏度
        （2）获取摄氏度，计算华氏度
        （3）获取摄氏度，计算开氏度
"""
# （1）获取华氏度，计算摄氏度
fahrenheit = eval(input("请输入华氏度:"))
centigrade = (fahrenheit - 32) / 1.8
print("{}华氏度={}摄氏度".format(fahrenheit, centigrade))

# （2）获取摄氏度，计算华氏度
centigrade = eval(input("请输入华氏度:"))
fahrenheit = fahrenheit * 1.8 + 32
print("{}摄氏度={}华氏度".format(centigrade, fahrenheit))

# （3）获取摄氏度，计算开氏度
centigrade = eval(input("请输入华氏度:"))
kelvin = centigrade + 273.15
print("{}摄氏度={}开氏度".format(centigrade, kelvin))

