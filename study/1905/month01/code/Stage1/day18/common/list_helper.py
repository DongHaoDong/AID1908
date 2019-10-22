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
    @staticmethod
    def is_exists(list_target,function_condition):
        """
            通用的判断是否存在某个条件元素的方法
        :param list_target:需要查找的列表
        :param function_condition:需要查找的条件，函数类型
            函数名(参数) --> bool
        :return:bool类型，True存在，False不存在
        """
        for item in list_target:
            if function_condition(item):
                return True
        return False
    @staticmethod
    def sum(list_target,function_handle):
        """
            通用的求和方法
        :param list_target:需要求和的列表
        :param function_handle:需要求和的处理逻辑，函数类型
            函数名(参数) --> int/float
        :return:和
        """
        sum_value = 0
        for item in list_target:
            sum_value += function_handle(item)
        return sum_value
    @staticmethod
    def select(list_target,function_handle):
        """
            通用的删选方法
        :param list_target:需要筛选的列表
        :param function_handle:需要筛选的处理逻辑，函数类型
            函数名(参数) --> int/str/元组/其他类型的数据
        :return:生成器
        """
        for item in list_target:
            yield function_handle(item)
    @staticmethod
    def get_max(list_target,function_handle):
        """
            通用的获取最大元素的方法
        :param list_target:需要搜索的列表
        :param function_handle:需要搜索的处理逻辑，函数类型
            函数名(参数) -->  int/str
        :return 最大元素
        """
        max_value = list_target[0]
        for index in range(1, len(list_target)):
            if function_handle(max_value) < function_handle(list_target[index]):
                max_value = list_target[index]
        return max_value
    @staticmethod
    def order_by(list_target,function_handle):
        """
            通用的升序排序方法
        :param list_target: 需要排序的数据
        :param function_handle: 需要排序的逻辑，函数类型
            函数名(参数) --> int/float需要比较的数据
        :return:
        """
        for row in range(len(list_target) - 1):
            for col in range(row + 1, len(list_target)):
                if function_handle(list_target[row]) > function_handle(list_target[col]):
                    list_target[row], list_target[col] = list_target[col], list_target[row]
