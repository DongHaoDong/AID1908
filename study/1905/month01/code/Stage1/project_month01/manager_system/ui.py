"""
    界面代码
"""
from bll import *
from model import *
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

    def __input__number(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入有误")


    def __input_student(self):
        name = input("请输入姓名：")
        # age = int(input("请输入年龄："))
        # score = int(input("请输入成绩："))
        age = self.__input__number("请输入年龄：")
        score = self.__input__number("请输入成绩：")
        student = StudentModel(name,age,score)
        self.__manager.add__student(student)

    def __output_students(self,list_ouput):
        for item in list_ouput:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        # id = int(input("请输入编号："))
        id = self.__input__number("请输入编号:")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        student = StudentModel()
        # student.id = int(input("请输入要修改的学生编号:"))
        student.id = self.__input__number("请输入要修改的学生编号:")
        student.name = input("请输入新的学生名称:")
        # student.age = int(input("请输入新的学生年龄:"))
        student.age = self.__input__number("请输入新的学生年龄:")
        # student.score = float(input("请输入新的学生成绩:"))
        student.score = self.__input__number("请输入新的学生成绩:")
        if self.__manager.update_student(student):
            print("修改成功")
        else:
            print("修改失败")

    def __output_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.student_list)