"""
    根据身高体重,参照BMI,返回身体状况
    BMI:用体重千克数除以身高米的平方得出的数值
    中国参考标准
    体重过低    BMI<18.5
    正常范围    18.5<=BMI<24
    超重       24<=BMI<28
    I度肥胖    28<=BMI<30
    II度肥胖   30<=BMI<40
    III度肥胖  BMI>=40.0
"""
while True:
    height = float(input("请输入身高(m)："))
    weight = float(input("请输入体重(kg)："))
    BMI = weight / pow(height, 2)
    if BMI < 18.5:
        print("BMI指数是{},体重过低".format(BMI))
    elif 18.5 <= BMI < 24:
        print("BMI指数是{},体重正常".format(BMI))
    elif 24 <= BMI < 28:
        print("BMI指数是{},体重超重".format(BMI))
    elif 28 <= BMI < 30:
        print("BMI指数是{},I度肥胖".format(BMI))
    elif 30 <= BMI < 40:
        print("BMI指数是{},II度肥胖".format(BMI))
    elif BMI >= 40:
        print("BMI指数是{},III度肥胖".format(BMI))
