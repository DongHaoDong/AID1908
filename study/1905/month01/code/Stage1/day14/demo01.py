"""
    内置可重写函数
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象 --> 字符串(随意格式)
    def __str__(self):
        return "我叫{},编号是{},年龄是{},成绩是{}".format(self.name, self.age, self.score,self.id)

    # 对象 --> 字符串(解释器可识别,有个事)
    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)"%(self.name, self.age, self.score, self.id)


s01 = StudentModel("无忌", 27, 100, 101)
str01 = str(s01)
print(str01)
print(s01)

str01 = repr(s01)
print(str01)
# 根据字符串执行python代码
result = eval("1+2*5")
print(result)
# 克隆对象
# repr返回python格式的字符串(创建对象)
s02 = eval(repr(s01))
print(eval(repr(s01)))
