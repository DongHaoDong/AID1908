# 搭建结构
```python
from flask import Flask  
app = Flask(__name__)  
@app.route("/路径")  
def fun():   
    return ""  
if __name__ == '__main__':
    app.run(debug=True,port=5555)
```
# 路由
```python
@app.route() #来表示路由  
@app.route('/') #访问路径/  
def url():
    return ''  
@app.route('/index') #访问路径/index  
def index():
    return ''  
@app.route('/user/info') #访问路径/user/info  
def userinfo():
    return ''  
@app.route('/user/<name>') #访问路径/user/xxx  
def user(name):  
    return ''
@app.route('/user/<int:age>') #访问路径/user/xxx
def user(age):
    # age是一个整数
    return ''
"""
类型转换器
默认：字符串，不允许有/
int:
float:
path:字符串(可以有/)
"""
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
@app.route('/index/<int:page>')
def index(page=None):
    return ''
# 路由的反向解析
url_for(funName,arg1=value1,arg2=value2)
# funName:要反向生成地址的函数名
# arg1 ~ n:传递给url的参数名和值
```
# Templates - 模板
1. 模板设置
    * 需要在flask程序文件夹中创建一个templates的子文件夹
2. 渲染模板
    * render_template():将模板渲染成字符串再响应
    * 语法:
        * render_template('xxx.html',arg1=value1,arg2=value2)
        * xxx.html:要渲染的模板文件
        * arg1 ~ n:要传递给模板的变量占位符
        * 返回值:字符串
3. 模板中的语法
    * 变量
        * 变量是一种特殊的占位符，告诉模板引擎盖位置的值是从渲染模板时的数据中来获取的
        * 在视图中:
            ```python
            @app.route('/')
            def index():
                return render_template('xxx.html',name='sf.zh',age=18)
            # name和age就是要传递到xxx.html中的变量
            ```
        * 在模板中:  
            {{变量名}}
        * 练习:在01_temp.html基础上，完成下列效果显示
            ```
            书名：《钢铁是怎么样炼成的》
            作者：奥斯特洛夫斯基
            价格: 32.5
            出版社：北京大学出版社
            ```
    * 过滤器
        * 什么是过滤器
            * 过滤器是允许在变量输出显示之前改变变量的值
        * 过滤器的语法
            * {{变量|过滤器}}
            * Jinja2 变量过滤器
            
            |过滤器名|说明|
            |-------|----|
            |capitalize|首字符变大写，其他字符边小写|
            |lower|把值转换成小写|
            |upper|把值转换成大写|
            |title|把值中的每个单词的首字符变大写|
            |trim|把值两端的空格去掉|
    * 控制结构
        * if结构
            ```
            {% if 条件  %}
            {% endif %}
          
            {% if 条件 %}
                条件满足执行
            {% else %}
                不满足条件执行
            {% endif %}
            ```
        * for结构
            ```
            {% for 变量 in 元组|列表|字典 %}
            {% endfor %}
            ```
    * 宏
        * 使用{% macro %}标签声明宏
            ```
            <!--声明-->
            {% mscro show(str) %}
                <h1>{{str}}</h1>
            {% endmscro %}
            <!--调用-->
            {{show(uname)}}
            ```
      
        1. 创建macro.html
            ```
            {% macro show(str) %}
                <h1>{{str}}<h1>
            {% endmacro %}
            {% macro show_li(str) %}
                <li>{{str}}</li>  
            {% endmacro %}
            ```
        2. 在使用的网页中，导入macro.html
            ```
            {% import 'macro.html' as macros %}
            {{ macros.show_li(uname) }}
            ```
    * 模板的包含
        * 在多处重复使用的模板代码可以放在单独的文件中，可以被其他的模板所包含(引用)
        * {% include 'xxx.html' %}
4. 静态文件
    * 什么是静态文件
        * 在Flask中不能与服务器动态交互的文件都是静态文件
        * 如css,js,图片,音视频,... ... 
    * 静态文件的处理
        * 所有静态文件都保存在项目文件夹中的static文件夹中
        * 在访问静态文件的时候需要通过/static/资源路径进行访问
        * <img src="/static/资源路径">
        * 反向解析:
            url_for('static',filename='<file_path>')
            <img src="{{url_for('static',filename='images/赵丽颖_1.jpg')}}">
5. 模板的继承
    * 什么是模板的继承  
        * 模板的继承类似于类的继承，如果一个模板中出现大量内容是另外一个模板的话，那么就可以使用继承的方式来简化开发  
    * 语法
        * 父模板中
            * 需要定义出哪些内容在子模板中是可以被重写的  
            {% block 块名 %}  
            {% endblock %}  
            block:定义允许在子模板中被修改的内容  
                * 在父模板中正常显示，没有任何影响
                * 在子模板中可以被重写
        * 子模板中
            * 使用{% extends '父模板名称' %} 来完成继承  
            * 使用{% block 块名 %}来重写父模板中的同名内容  
            {% block 块名 %}    
                覆盖掉父模板中的内容  
            {% endblock %}  
            * 允许通过{{super()}}来调用父模板中的内容  
          
    
# 自定义错误页面
1. 404错误处理  
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
```
2. 500错误处理  
```python
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500
```