# SQLAlchemy - 查询
1. 基于 db.session
    1. db.session.query()
        - 参数：实体，多个实体，实体中的属性
        - 返回值：BaseQuery()
        1. 查询执行函数
            1. all()
            2. first()
            3. first_or_404()
            4. count()
        2. 查询过滤器
            1. filter()
            2. filter_by()
            3. limit()
                - limit.offset()
            4. order_by()
            5. group_by()
2. 基于Models
    1. Model.query.查询过滤器().查询执行函数()
# SQLAlchemy - 删除、修改
1. 删除：db.session.delete(model)
    - model:要删除的实体对象
2. 修改：  
    1.查2.改3.保存
# 关系映射
Teacher: id,tname,tage(多)  
Course: id,cname(一)  
一名老师只能教一门课程  
一门课程可以由多个老师来教  
数据库实现:
- 在"多"表中增加外键引用自"一"表中的主键
```python
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column()
    # Teacher中会存在一个隐式属性:course
    teacher = db.relationship('Teacher',backref='course',lazy='dynamic')
class Teacher(db.Model):
    id = db.Column()
    tname = db.Column()
    course_id = db.Column(db.Integer,db.ForeignKey('course_id'))
```
# 关系映射
1. 一对多
    - 语法
        1. "多"实体中
            - 外键列名=db.Column(db.Integer,db.ForeignKey('主表.主键'))
        2. "一"实体中
            - 增加反向引用关系
            - 属性名=db.relationship('多表实体类名',关系选项)
            - 常用的关系选项
            
            |选项名|说明|
            |-----|----|
            |backref|在关系的另一个模板中添加反向引用|
            |lazy|指定如何加载相关记录|
            |lazy|select:首次访问时加载|
            |lazy|immediate:源对象加载后立马加载|
            |lazy|subquery:立即加载,但使用子查询|
            |lazy|noload:永不加载|
            |lazy|dynamic:不加载记录，但提供加载记录的查询|
            |uselist|如果设置False,则不使用列表,使用标量|
            |secondary|指定多对多关系中关联表的名字|
2. 一对一
    1. 什么是一对一
        - A表中的一条记录只能与B表中的一条记录关联
        - B表中的一条记录只能与A表中的一条记录关联
    2. 在数据库中的体现
    3. SQLAlchemy
    ```python
       class Wife(db.Model):
           teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))
       class Teacher(db.Model):
           wife = db.relationship('Wife',backref="teacher",uselist=False)
    ```
3. 多对多
    1. 什么是多对多
        - A表中的一条数据可以与B表中的任意多条数据关联
        - B表中的一条数据可以与A表中的任意多条数据关联
    2. 多对多实现
        - 使用第三张表来关联(并不需要实体类)
        1. 创建第三张表
        ```
           student_course = db.Table(
                "student_course",# 在数据库中的表名
                db.Column('id',db.Integer,primary_key=True),# 该表的主键
                db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                db.Column('course_id',db.Integer,db.ForeignKey('course.id')),
            )
        ```
        2. 增加关联属性以及反向引用
            ```python
               class Student(db.Model):
                   courses = db.relationship(
                       "Course",
                       secondary='student_course',
                       lazy='dynamic',
                       backref=db.backref('students',lazy='dynamic')
                   )
            ```
            


