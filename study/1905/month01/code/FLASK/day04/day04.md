# 请求对象- request
from flask import request  
属性  
    1. request.method  
    2. request.args  
    3. request.form  
    4. request.cookies  
    5. request.headers  
1. 获取get请求数据  
    使用超链接发送get请求，拼地址参数
    ```
    <a href="/request?name=zsf&age=85">xxx</a>
    name = request.args.get("name")
    age = request.args.get("age")
    使用js中的location对象，发送get请求并发送拼接参数
    <script>
        $btn.click(function(){
            location.href="xxxx?arg1=value1&arg2=value2"
        });
    </script>
    ```
2. 获取post请求数据
    request.form.get('xxx')
    request.form.getlist('name_list')
# 响应对象
除了可以响应的字符串和模板之外，还可以是响应对象或重定向
1. 响应对象 - make_response()   
```
from flask import make_response  
resp = make_response('xxx')  
return resp  
resp = make_response(render_template('xx.html',params=locals())  
return resp
```
2. 重定向  
由服务器通知浏览器向新的地址发送一个请求  
```
from flask import redirect
resp = redirect('重定向地址')
return resp
```
# 文件上传
1. 前端页面 
    1. form中的method的值必须为post
    2. form中的enctype的值必须为multipart/form-data  
    大量数据上传的时候(如:超大文件)，就不能使用网页上传了(主要是由于http协议不支持)，需要使用单独的山川工具(C/S版的)
2. 服务器端
    1. 使用request.files接收上传的文件    
    request.files['文件选择框名称']  
    f.save('static/'+f.filename)  
    os.path.dirname(__file__)  
    os.path.join(目录1,目录2,目录3)  
# 模型 - Models
1. 什么是模型  
模型，是根据数据库中表的结构来创建出来的class。每张表到编程语言中就是一个class,表中的每一个列，到编程语言中就是class中的一个属性
2. 创建和使用模型 ORM
    1. 什么是ORM  
    ORM:Object Relational Mapping  
    简称：ORM,O/RM,O/R Mapping  
    中文：对象关系映射  
    2. ORM的三大特征
        1. 数据表(Table)到编程类(class)的映射  
        数据库中的每一张表对应到编程语言中，都有一个类   
        在ORM中  
        允许将数据表自动生成一个类  
        也允许将类自动生成一张表  
        2. 数据类型的映射  
        将数据库表中的字段以及数据类型对应到编程语言中类的属性  
        在ORM中  
        允许将表中的字段和数据类型自动映射到编程语言中  
        也允许将类中的属性和类型也映射到数据库表中  
        3. 关系映射  
        将数据库中表之间的关系对应到编程语言中类之间的关系  
        数据库表之间的关系：  
        一对一，一对多，多对多  
        一对一:主外键关联，外键需要加唯一约束  
        一对多:主外键关联  
        多对多:
        
        ORM的优点
        1. 提高了开发的效率
        2. 可以省略庞大的数据访问层，即便不使用SQL编码也能完成对数据的CRUD操作  
3. 定义模型
    1. 数据库和框架的配置
        1. 安装SQLAlchemy
        pip install sqlalchemy  
        pip install flask-sqlalchemy
        2. 创建数据库  
        create database flask default charset utf8 collate utf8_general_ci;
        3. 配置数据库  
        ```python
        from flask import Flask
        # 将SQLALchemy导入进来
        from flask_sqlalchemy import SQLALchemy
        app = Flask(__name__)
        # app.config['SQLALCHEMY_DATABASE_URI']="mysql://username:pwd@host:port/dbname"
        app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:584023982@127.0.0.1:3306/flask"
        # 创建SQLALchemy的实例
        db = SQLALchemy(app)
        # db是SQLALchemy的实例，表示程序正在使用的数据库，同时也获得了SQLALchemy中的所有功能
        
        
        if __name__ == '__main__':
            app.run(debug=True)
        ```
    2. 定义模型
        1. 模型:数据库中的表在编程语言中的体现，其本质就是一个python的类(可称为:模型类或实体类)，类中的属性要与数据表中的列相对应
        2. 语法
            ```python
            class MODELNAME(db.Model):
               __tablename__ = "TABLENAME"
               COLUMN_NAME = db.Column(db.TYPE,OPTIONS)
            ```
            1. MODELNAME:定义模型类名称，根据表名指定
            2. TABLENAME：映射到数据库中表的名字
            3. COLUMN_NAME:属性名，映射到数据库表中列的名字
            4. db.TYPE:映射到列的数据类型
            5. OPTIONS:列选项  
        
        db.TYPE列类型如下:
        
        |类型名|python类型|说明|
        |------|---------|----|
        |Integer|int|普通整数32位|
        |SmallInteger|int|小范围整数通常是16位|
        |BigInteger|int或long|不限精度的整数|
        |Float|float|浮点数|
        |Numeric|decimal.Decimal|定点数|
        |String|str|变长字符串|
        |Text|str|变长字符串，优化|
        |Unicode|unicode|变长Unicode字符串|
        |UnicodeText|unicode|优化后的变长Unicode|
        |Boolean|bool|布尔值|
        |Date|datatime.date|日期|
        |Time|datatime.time|时间|
        |DateTime|datetime.datetime|日期和时间|
        
        OPTIONS 列选项
        
        |选项名|说明|
        |------|----|
        |primary_key|设置True则表示该列为主键|
        |unique|设置为True则表示该列的值唯一|
        |index|设置为True则表示该列要创建索引|
        |nullable|设置为True表示该列的值允许为空|
        |default|为该列定义默认值|
    
    * 练习  
        1. 创建Student模型类  
            表名：student    
            字段:  
                1. id,主键,自增  
                2. sname,长度为30的字符串，不允许为空  
                3. sage,整数   
        2. 创建Teacher模型类    
            表名:teacher     
            字段:  
                1. id,主键,自增  
                2. tname,长度为30的字符串  
                3. tage,整数  
        3. 创建Course模型类  
            表名:course   
            字段:
                1. id,主键自增
                2. cname,长度为30的字符串
4. 数据库操作
    1. 插入
        db.session.add(Models)
        db.session.commit()
        
                
                
                
                
                
                
                
                    
                         
        







    
    







