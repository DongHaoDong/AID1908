"""
    静态方法
        将函数转移到类中
    总结
        实例方法：操作对象的数据
        类方法：操作类的变量
        静态方法：既不需要操作实例变量也不需要操作类的变量
"""
list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

class Vector2:
    """
        二维向量
        可以表示位置/方向
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # 静态方法：表示左边方向
    @staticmethod
    def left():
        return Vector2(0,-1)
    # 静态方法：表示右边方向
    @staticmethod
    def right():
        return Vector2(0,1)
# 作用:位置 + 方向
pos01 = Vector2(1,2)
# 通过类名调用静态方法
l01 = Vector2.left()
pos01.x += l01.x
pos01.y += l01.y
print(pos01.x,pos01.y)
class DoubleListHelper:
    # 在二维列表中获取指定位置的，某个方向的，指定数量的元素
    # 例如：list01 "10" 右边 3 --> "11", "12", "13"
    # 例如：list01 Vector(1,0) Vector.right() 3 --> "11", "12", "13"
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
        在二维列表中获取的指定位置，指定方向的，指定数量的元素
        :param target: 二维列表中
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向
        :param count: 指定数量
        :return:
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result
list_result = DoubleListHelper.get_elements(list01,Vector2(1,0),Vector2.right(),3)
print(list_result)
# 例如： list01 "23" 左边 2
list_result = DoubleListHelper.get_elements(list01,Vector2(2,3),Vector2.left(),2)
print(list_result)
