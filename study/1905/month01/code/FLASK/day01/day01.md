# 静态网页与动态网页
1. 静态网页：无法与服务器进行交互的网页
2. 动态网页：能够与服务器进行交互的网页
# WEB与服务器
1. WEB：网页(HTML,CSS,JS)
2. 服务器
* 能够给用户提供服务的机器就是服务器
    * 硬件与软件
        * 硬件范畴：一台主机
        * 软件范畴：一个能够接受用户请求并给出响应的程序
            * APACHE
            * TOMCAT
            * IIS(Internet Information Service)
            * Nginx
    * 作用
        * 存储WEB所需要的信息
        * 能够处理用户的请求(request)并给出响应(response)
        * 能够执行服务端程序
        * 具备一定的安全功能
# 框架
1. 什么是框架
    * 框架是一个为了解决开放性问题而存在的一种结构。框架本身也提供了一些最基本的功能，我们只需要在基础功能上搭建属于自己的操作即可
2. Python WEB框架
    * flask
    * django
    * tornado
    * webpy
    * WEB重点:请求，响应，数据
# Flask框架
1. 什么是Flask
    * Flask是一个基于Python并且依赖于Jinja2模板引擎和Werkzeug WSGI服务的一个微型框架
    * WSGI:Web Server Gateway Interface(WEB服务网关接口)
2. Flask的框架模式 - MTV
    * M:Models,模型层，负责数据库建模
    * T:Templates,模板层，用于处理用户显示的内容，如html
    * V:Views,视图层，处理与用户交互的部分内容。处理用户的请求并给出响应
3. 经典的三层结构：MVC
    * M:Models,模型层，负责数据库建模
    * V:Views，视图层，用于处理用户显示部分内容如html
    * C:Controller,控制器，处理与用户交互的部分内容，处理用户的请求与响应
# Flask 实现
1.  安装flask
    * pip install flask
2. 查看python已安装的flask版本
    * import flask
    * flask.\_\_version__
    * flask官网：https://falsk.pocoo.org/
3. 初始化
    * 见代码
    访问路径：http://localhost:5000/login:显示登陆页面
    访问路径：http://localhost:5000/register:显示注册页面
# Flask - 路由(route)
1. 什么是路由
    * 客户端将请求发送给Web服务器，Web服务器再将请求发送给flask程序实例
    * 程序实例需要知道每个url请求要运行哪些代码，所以需要建立一个url到python函数的映射，处理url和函数之间的关系的程序就是路由
    * 在Flask中，路由是通过@app.route装饰器来表示的
2. 路由的体现
    * 路由的基本表示
        ```python
        @app.route('/')
        def index():
          return "xxx"
        @app.route('/login')
        def login():
          return 'xxx'
        ```    
    * 带参数的路由
        * http://localhost:5000/show/sf.zh
        * http://localhost:5000/show/wj.zh
        * http://localhost:5000/show/zhouzhiruo
        1. 基本带参路由
        @app.route('/show/<name>')
        def show1(name):
            在函数中name表示的就是地址栏上传递过来的数据
            return 'xxx'
        2. 带多个参数的路由
           - localhost:5000/show2/sf.zh/85
           - localhost:5000/show2/wj.zh/18
           - localhost:5000/show2/ss.yin/30  
           @app.route('/show2/\<name>/\<age>')  
           def show2(name,age):
              return "xxx"  
        3. 指定参数类型的路由  
        @app.route('/show3/\<name>/\<int:age>')  
        def show3(name,age):
            return "xxx"  
        \<int:age>：表示age参数时一个整型的数值而非默认的字符串
            int:类型转换器  
            Flask中所支持的类型转换器  
            
            |类型转换器|作用|
            |---------|----|
            |缺省|字符串型，但不能有/(斜杠)|
            |int:|整型|
            |float:|浮点型|
            |path:|字符串型，可以有/(斜杠)|
        
        4. 多URL的路由匹配  
        允许在一个视图处理函数中设置多个url路由规则  
        @app.route('/')  
        @app.route('/index')  
        def index():  
            return "xxx"  
        5. 路由中设置HTTP请求方法:  
            Flask路由规则页允许设置对应的请求方法，只有将匹配上请求方法的路径交给视图处理函数去执行  
            @app.route('/post',methods=['POST'])  
            def post():  
                return "xxx"  
            说明：只有post请求方式允许访问localhost:5000/post
        6. URL的反向解析  
            正向解析:程序自动解析，根据@app.route()中的访问路径来匹配处理函数  
            反向解析:通过视图处理函数的名称自动生成视图处理函数的访问路径  
            Flask中提供了url_for()函数，用于反向解析url  
            第一个参数:指向函数名(通过@app.route()修饰的函数)  
            后续的参数们:对应要构建的url上的变量  
            ex:  
                @app.route('/')  
                def index():  
                    return "Index"  
                @app.route('/show/<name>')  
                def show(name):  
                    return "name:{}".format(name)   
                1. url_for('index'):结果为:/  
                2. url_for('show',name='zsf'):结果为:/show/zsf  
            特殊：
                url_for('static',filename='style.css')  
                静态文件反向解析  
# 模板 - Templates
1. 什么是模板
    * 模板是一个包含响应文本的文件(通常是html),该文件中允许包含"占位变量"来表示动态的内容，其具体值在请求中才能知道。"占位变量"最终会被真实的值锁替换
    * 模板最终也会被解析成响应的字符串，这一过程被称为"渲染" 
    * Flask实际上是使用Jinja2强大的模板引擎
2. 模板的设置
    * 默认情况下,Flask会在程序文件夹中的templates子文件夹中寻找模板  
    * 需要手动创建templates文件夹
3. 渲染模板
    * 在视图函数中通过
        * return render_template()将模板渲染成字符串再响应给客户端
        * render_template()语法:
            * render_template('xxx.html',arg1=value1,arg2=value2)
            * 参数1:xxx.html，要渲染给客户端的html模板文件
            * 参数2~n:要传递给模板动态显示的变量占位符，如果没有动态的变量占位符，则可以省略
            * 返回值:字符串
    

              
                
            
        
            
    
    