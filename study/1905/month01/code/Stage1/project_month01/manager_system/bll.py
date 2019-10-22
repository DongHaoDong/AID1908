"""
    定义业务逻辑处理
"""
class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量，表示初始变量
    __init_id = 1000

    def __init__(self):
        self.__student_list = []

    @property
    def student_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__student_list

    def add__student(self,student_info):
        """
            添加一个新学生
        :param student_info:没有编号的学生信息
        """
        student_info.id = self.__generate_id()
        self.__student_list.append(student_info)

    def __generate_id(self):
        """
            学生id生成器
        :return:
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,id):
        """
            根据id删除学生
        :param id: 学生编号
        :return:
        """
        for item in self.__student_list:
            if item.id == id:
                self.__student_list.remove(item)
                return True     # 移除成功
        return False            # 移除失败

    def update_student(self,student_info):
        """
            根据student_info.id修改其他信息
        :param student_info:学生对象
        :return:
        """
        for item in self.__student_list:
            if item.id == student_info.id:
                item.name = student_info.name
                item.age = student_info.age
                item.score = student_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩对self.__student_list进行升序排列
        """
        for row in range(len(self.__student_list)-1):
            for col in range(row+1,len(self.__student_list)):
                if self.student_list[row].score > self.__student_list[col].score:
                    self.__student_list[row],self.__student_list[col] = self.__student_list[col],self.__student_list[row]