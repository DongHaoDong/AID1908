# 模板的语法
1. 变量
    1. 在视图中:  
        return render_template('xx.html',变量1=值1，变量2=值2)  
        return render_template('xx.html',params=locals())  
        允许传递到模板中的数据类型:  
        数字，字符串，字典列表，元组，对象
    2. 在模板中:  
        {{变量}}  
        {{uname}}  
        {{list[1]}}或{{list.1}}  
        {{person.show()}}
2. 过滤器
    1. 在变量输出之前改变变量的值  
    {{变量|过滤器}}  
    过滤器:  
    lower  
    upper  
    capitalize
    trip  
3. 控制结构
    1. if 结构  
        {% if 条件 %}  
        满足条件要执行的代码块(html/变量/过滤器)  
        {% endif %}  
        {% if 条件 %}  
        满足条件要执行的代码块(html/变量/过滤器)  
        {% else %}  
        不满足条件执行的代码块
        {% endif %}  
    2. for 结构  
        {% for 变量 in 列表, 元组,字典 %}  
        {% endfor %}  
    3. 宏  
        {% macro 函数名() %}  
        函数体(html/变量/过滤器)  
        {% endmacro %}  
        调用:
        {{ 函数名() }}  
        允许将宏声明在独立的网页中:  
        1. 创建网页 - macro.html  
        {% macro 函数名() %}  
        函数体(html/变量/过滤器)  
        {% endmacro %}
        2. 在网页中导入macro.html  
        {% import 'macro.html' as macros %}  
        {{ macros.函数名() }}
    4. 模板的包含  
        {% include 'xxx.html' %}  
4. 静态文件
    1. 在项目目录中创建static目录用于保存静态文件
    2. 在模板中使用静态文件  
    /static/...  
    \<img src="/static/img/xxx.jpg">  
    \<img src="{{url_for('static',filename='img/a.jpg')}}" 
5. 继承  
    1. 父模板中  
        {% block 块名 %}  
        {% endblock %}  
        block作用:定义在子模板中允许被修改的内容部分
        1. 在父模板中是被正常显示的  
        2. 在子模板中可以被重写     
    2. 子模版中  
        1. 使用{% extends '父模板名称' %} 实现继承
        2. 使用{% block 块名 %}..{% endblock %}  
           覆盖父模板中的同名内容  
        3. 使用{{super()}} 调用父模板中的内容 
           
    
          
# 修改配置
app = Flask(__name__,template_folder='muban',static_url_path='/s',static_folder='s')
1. template_folder  
    设置模板的保存路径
2. static_url_path  
    设置静态文件的访问路径
3. static_folder(映射得到WEB中的访问路径)  
    设置静态文件的保存目录(映射到项目中的目录名称)
# 请求(request)和响应(response)
1. HTTP协议
2. 请求对象 - request
    1. request - 请求对象，封装了所有与请求相关的信息，如:  
    请求消息头，请求数据，请求路径，...  
    在Flask中，请求信息被封装到request对象中  
    from flask import request
    2. request的成员(常用)
        1. scheme:获取请求方案(协议)
        2. method:获取本次请求的请求方式
        3. request.args:获取使用get方式提交的数据
        4. request.form:获取使用post方式提交的数据
        5. request.values:获取GET和POST请求方式提交的数据(GET,POST通用)
        6. request.cookies:获取cookies中的信息
        7. request.headers:请求消息头信息
        8. request.path:获取请求的url地址
        9. request.files:获取用户上传的文件
        10. request.full_path:获取完整路径
        11. request.url:获取访问地址
    3. 获取请求提交的数据
        1. get方式  
            get请求的数据放在QueryString中  
            request.args封装的就是get请求的数据，类型为字典
            request.args['name']：获取name对应的值
            request.args.get('name')：获取name对应的值
            request.args.getlist('name_list')：获取name_list 列表数据
        2. post请求方式  
            post请求的数据是放在form中的  
            request.form封装的是就是post请求的数据，类型为字典
            request.form['name']：获取name对应的值
            request.form.get('name')：获取name对应的值
            request.form.getlist('name_list')：获取name_list 列表数据  
            练习:  
            1. 访问地址localhost:5000/post,能够去往04-form.html  
            包含一个表单，post请求方式，提交地址自定义  
                1. 文本框，用户名
                2. 密码框，密码
                3. 邮箱框，邮箱<input type="email">
                4. 文本框，真实姓名
                5. 提交按钮
            2. 提交时，提交到post_do
            3. post_do  
                获取所有请求提交的数据，并打印在终端上
3. 响应对象  
    响应对象其实就是要响应给客户端的内容，可以是普通字符串，也可以是模板或者是重定向  
    @app.route('/')  
    \# return "Hello World"  
    return render_template('xxx.html')  
    \# 以上两种行为，本质上响应回去的都是字符串  
    1. 构建响应对象，响应给客户端  
    注意:不是直接响应字符串，而是响应对象  
    响应对象可以包含响应的字符串，同时也可以实现其他的响应操作   
    在flask中，使用make_response()构建响应对象  
    from flask import make_response  
    resp = make_response('响应内容')  
    \# 实现其他操响应操作，如添加cookies  
    return resp  
    2. 重定向  
        1. 什么是重定向    
            由服务器端通知客户端重新向新的地址发送请求  
        2. 语法  
            form flask import redirect  
            resp = redirect('重定向地址'')
            return resp
4. 文件上传  
    1. 注意问题  
        表单中提交方式必须为post  
        enctype属性设置为multipart/form-data  
    2. 服务器端  
        1. 通过request.files获取上传的文件  
            f = request.files['文件框name属性值']  
        2. 通过f.save(并保存路径)将文件保存到指定目录处  
            通过f.filename获取文件的名称  
            filename = f.filename
            f.save('static/'+filename)
        
    
    
    
                
            
            
            
        
        
        
            
    
    