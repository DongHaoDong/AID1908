"""
[
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]
"""
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
    # 静态方法：表示上边方向
    @staticmethod
    def up():
        return Vector2(-1, 0)
    # 静态方法：表示上边方向
    @staticmethod
    def down():
        return Vector2(1, 0)
class DoubleListHelper:
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

# 被其他模块导入使用
# 以下为财务室代码，只有从前端模块运行才会执行
if __name__ == "__main__":
    list01 = [
        ["00","01","02","03"],
        ["10","11","12","13"],
        ["20","21","22","23"],
    ]
    # 在二维列表中，获取13的位置，向左，3个元素
    result = DoubleListHelper.get_elements(list01,Vector2)
