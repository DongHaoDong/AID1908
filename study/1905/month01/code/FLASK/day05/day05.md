# 模型
使用名为SQLAlchemy的ORM框架，并且需要Flask-SQLAlchemy  
配置 
```python
from flask_sqlalchemy import SQLAlchemy  
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@host:port/dbname"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
``` 

1. 定义模型
```
class MODELNAME(db.Model):
    __tablename__ = "TABLENAME"
    COLUMN_NAME = db.Column(db.TYPE,OPTIONS)
```
- Flask-SQLALCHEMY - 查询
    - db.session进行查询
        - db.session.query()
            - 该函数会返回一个Query对象，类型为BaseQuery,包含了指定实体类对应的表中所有的数据
            - 该函数也可以接受多个参数，参数表示的是要查询哪个实体
        - 查询执行函数
            - 目的:在查询的基础上得到最终想要的结果
            - 语法:db.session.query(...).查询执行函数()  
            
            |函数|说明|
            |----|----|
            |all()|返回查询的所有结果|
            |first()|返回查询中的第一个结果,如果没有结果,则返回None|
            |first_or_404()|如果没有结果,则终止并返回404|
            |count()|返回查询结果的数量|
        - 查询过滤器函数
            - 作用:在查询的基础上，筛选部分列出来
            - 语法:db.session.query().过滤器函数().查询执行函数()
            - 过滤器函数
            
            |函数|说明|
            |----|----|
            |filter()|按指定条件进行过滤(多表，单表，定值，不定值)|
            |filter_by()|按等值条件进行过滤|
            |limit()|按限制行数进行获取|
            |order_by()|根据指定条件进行排序|
            |group_by()|根据指定条件进行分组|
            - 详解:
            1. filter()
                1. 查询年龄大于30的Users的信息
                db.session.query(Users).filter(Users.age>30).all()  
                注意:条件必须由模型类.属性来组成
                2. 查询年龄大于30且id大于5的Users信息
                db.session.query(Users).filter(Users.age>30,Users.id>5).all()
                3. 查询年龄大于30或者id大于5的Users的信息  
                注意:查询或的操作，要借助or_()  
                db.session.query(Users).filter(or_(条件1,条件2))
                4. 查询id=5的Users的信息  
                注意:等值判断必须使用==
                db.session.query(Users).filter(Users.id==5).first()
                5. 查询email中包含'w'的users的信息-模糊查询like  
                db.session.query(Users).filter(Users.email.like('%d%'))
                6. 查询id在[1,2,3]之间的Users信息
                db.session.query(Users).filter(Users.id.in_([1,2,3]))
            2. filter_by()
                1. 查询id=5的Users的信息
                db.session.query(Users).filter_by(id=3).first()
            3. limit()
                1. 在整个查询结果中获取前5条数据
                db.session.query(Users).limit(5).all()
            4. order_by()
                1. 对Users表中所有的数据按id倒序排序
                    db.session.query(Users).order_by(Users.id.desc(),Users.age.asc()).all()
            5. group_by()
                db.session.query(Users).group_by('age').all()
    - 基于Models进行查询  
        Models.query.查询过滤器(条件参数).查询执行函数()
- Flask-SQLALCHEMY - 删除和修改
    1.  删除
        1. 查询出要删除的实体
        user = db.session.query(Users).filter_by(id=5).first()
        db.session.delete(user)
        2. 根据所提供的删除方法将信息删除
    2. 修改  
        将id为4的用户名改为张乐乐
        1. 查
        user = Users.query.filter_by(id=4).first()
        2. 改
        user.username = "张乐乐"
        user.age = "23"
        user.email = "zhanglele@163.com"
        3. 保存
        db.session.add(user)
- FLASK-SQLALCHEMY - 关系映射
    1. 一对多
        - 语法实现
            1. 在"多"实体中增加
                - 外键列名=db.Column(db.Integer,db.ForeignKey('主表.主键'))
            2. 在"一"实体中增加反向引用关系
                - 属性名=db.relationship('多的实体类名',backref="属性名",lazy="dynamic")
                
Teacher & Course  
每名Teacher只能教一门Course  
每门Course可以由多个Teacher来教

