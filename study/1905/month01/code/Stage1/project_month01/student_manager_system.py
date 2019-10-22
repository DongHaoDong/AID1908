"""
    学生管理系统
    项目计划
        1.完成数据模型类StudentModel
        2.创建完成逻辑控制类StudentManagerController
        3.完成数据：学生列表__student_list
        4.行为：获取学生列表student_list
        5.添加学生add_student
        6.根据编号删除学生remove_student
        7.根据编号修改学生update_student
        8.在视图类中根据编号删除学生remove_student
        9.在视图类中根据编号修改学生remove_student
"""
class StudentModel:
    """
        学生信息模型
    """
    def __init__(self,name="",age=0,score=0,id=0):
        """
            创建学生对象
        :param name: 姓名，类型str类型
        :param age: 年龄，int类型
        :param score: 成绩，float类型
        :param id: 编号(该学生对象的唯一标识)
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

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

class StudentManagerView:
    """
        学生管理器视图
    """
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("[1]添加学生")
        print("[2]显示学生")
        print("[3]删除学生")
        print("[4]修改学生")
        print("[5]按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.student_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_by_score()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = float(input("请输入成绩："))
        student = StudentModel(name,age,score)
        self.__manager.add__student(student)

    def __output_students(self,list_ouput):
        for item in list_ouput:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = int(input("请输入编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        student = StudentModel()
        student.id = int(input("请输入要修改的学生编号:"))
        student.name = input("请输入新的学生名称:")
        student.age = int(input("请输入新的学生年龄:"))
        student.score = float(input("请输入新的学生成绩:"))
        if self.__manager.update_student(student):
            print("修改成功")
        else:
            print("修改失败")

    def __output_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.student_list)


view = StudentManagerView()
view.main()

"""
    测试添加学生信息功能
    manager = StudentManagerController()
    s01 = StudentModel("zs",24,100)
    manager.add__student(s01)
    manager.add__student(StudentModel("ls",25,95))
    for item in manager.student_list:
        print(item.id)
        print(item.name)
        print(item.age)
        print(item.score)
"""

"""
    # 测试删除学生
    manager = StudentManagerController()
    manager.add__student(StudentModel("zs"))
    manager.add__student(StudentModel("ls"))
    print(manager.remove_student(1003))
    for item in manager.student_list:
        print(item.id,item.name)
"""


"""
    测试修改学生
    manager = StudentManagerController()
    manager.add__student(StudentModel("zs"))
    manager.add__student(StudentModel("ls"))
    for item in manager.student_list:
        print(item.id,item.name,item.age,item.score)
    manager.update_student(StudentModel("张三",23,84,1001))
    print("修改后...")
    for item in manager.student_list:
        print(item.id,item.name,item.age,item.score)# 测试修改学生
"""






