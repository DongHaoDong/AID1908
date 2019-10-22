"""
    自定义异常类
"""
class AgeError(Exception):
    """
        年龄错误
    """
    def __init__(self,message,age_value,code_line,error_nummber):
        super.__init__("出错啦")
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_nummber


class Wife:
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 21 <= value <=31:
            self.__age = value
        else:
            # raise ValueError("我不要")
            raise AgeError("超过我想要的范围了",value,24,1001)
try:
    w01 = Wife(81)
except AgeError as e:
    print("请重新输入")
    print(e.message)
    print(e.age_value)
    print(e.code_line)
    print(e.error_number)
