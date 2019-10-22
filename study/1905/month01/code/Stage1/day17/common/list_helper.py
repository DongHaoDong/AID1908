"""
    列表助手模块
"""
class ListHelper:
    """
        列表助手类
    """
    @staticmethod
    def find_all(list_target,function_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target:需要查找的列表
        :param function_condition:需要查找的条件，函数类型
            函数名(参数) --> bool
        :return:需要查找的元素,生成器类型
        """
        for item in list_target:
            if function_condition(item):
                yield item
    @staticmethod
    def find_single(list_target,function_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target:需要查找的列表
        :param function_condition:需要查找的条件，函数类型
            函数名(参数) --> bool
        :return:需要查找的元素
        """
        for item in list_target:
            if function_condition(item):
                return item
    @staticmethod
    def get_count(list_target,function_duration):
        """
            通用的计算满足某个条件的元素数量方法
        :param list_target:需要查找的列表
        :param function_duration:需要查找的条件，函数类型
            函数名(参数) --> bool
        :return:满足条件元素的个数
        """
        count_value = 0
        for item in list_target:
            # if item.duration <= 5:
            if function_duration(item):
                count_value += 1
        return count_value