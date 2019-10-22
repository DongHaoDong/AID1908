"""
    敌人类(攻击力0--100)
        抛出异常的信息:消息/错误行/攻击力/错误编号
"""
class AtkError(Exception):
    """
        攻击错误
    """
    def __init__(self,message,atk_value,code_line,error_nummber):
        super.__init__("出错啦")
        self.message = message
        self.atk_value = atk_value
        self.code_line = code_line
        self.error_number = error_nummber
class Enemy:
    def __init__(self,atk):
        self.atk = atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 0 <= value <=100:
            self.__atk = value
        else:
            # raise ValueError("我不要")
            raise AtkError("超过我想要的范围了",value,24,1001)
try:
    e01 = Enemy(81)
except AtkError as e:
    print("请重新输入")
    print(e.message)
    print(e.atk_value)
    print(e.code_line)
    print(e.error_number)