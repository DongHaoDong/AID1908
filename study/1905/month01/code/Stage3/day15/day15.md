# POST传递参数
* 客户端通过表单等POST请求将数据传递给服务器端，如：
```html
<form method="post" action="/user/login">
    姓名:<input type="text" name="username">
</form>
```
* 服务器端接收参数
    * 通过request.method来判断是否为POST请求，如:
    ```
    if request.method == 'POST':
        处理POST请求的数据并响应
    else:
        处理非POST请求并响应
    ```
* 使用post方式接收客户端数据
    1. 方法
    ```
    request.POST['参数名'] # request.POST 绑定QueryDict
    request.POST.get('参数名','')
    request.POST.getlist('参数名')
    ```
* 取消csrf验证，否则Django将会拒绝客户端发来的POST请求
    * 取消csrf验证
        * 删除settings.py中MIDDLEWARE中的CsrfViewsMiddleWare的中间件
        ```
        MIDDLEWARE = [
            ...
            # 'django.middleware.csrf.CsrfViewMiddleware',
            ...
        ]
        ```
# from 表单的name属性
* 在form控件提交数据时，会自动搜索本表单控件内部的子标签的name属性及相应的值，再将这些名字和值以键-值对的形式提交给action指定的服务器相关位置
* 在form内能自动搜集到的name属性的标签控件有
    ```html
    <input name="xxx">
    <select name="yyy"></select>
    <textarea name="zzz"></textarea>
    ```
    * 如:
    ```html
    <form action="/page1" method="post">
      <input name="title" type="text" value="输入">
      <select name="gender">
          <option value="1">男</option>
          <option value="0">女</option>
      </select>
      <textarea name="comment"cols="5" rows="10">附言...</textarea>
      <input type="submit" value="提交">
    </form>
    ```
# Django的框架设计模式
* MVC设计模式
    * MVC代表Model-View-Controller(模型-视图-控制器)模式。
    * 作用:降低模块间的耦合度(解耦)
    * MVC
        * M 模型层(Model),主要用于对数据库层的封装
        * V 视图层(View),用于向用户展示结果
        * C 控制(Controller,用于处理请求、获取数据、返回结果(重要))
    * MVC模式如图:
        ![mvc](mvc.jpg)
* MTV模式
MTV代表Model-Template-View(模型-模板-视图)模式。这种模式用于应用程序的分层开发
    * 作用：
        * 降低模块间的耦合度(解耦)
    * MTV
        * M -- 模型层(Model)负责与数据库交互       
        * T -- 模板层(Template)负责呈现内容到浏览器
        * V -- 视图层(View)是核心，负责接收请求、获取数据、返回结果
    * MTV模式如图:
        ![mtv](mtv.jpg)
# 模板 Templates
* 什么是模板
    1. 模板是可以根据字典数据动态变化的html网页
    2. 模板可以根据视图中传递的字典数据动态生成对应的HTML网页
* 模板的配置
    * 创建模板文件夹<项目名>/templates
    * 在settings.py中有一个TEMPLATES变量
        1. BACKEND:指定模板的引擎
        2. DIRS:模板的搜索目录(可以是一个或多个)
        3. APP_DIRS:是否要在应用中的templates文件夹中搜索模板文件
        4. OPTIONS:有关模板的选项
    * 默认的模块文件夹templates
    * 修改settings.py文件，设置SEMPLATES的DIRS值为'DIRS'
      [os.path.join(BASE_DIR,'templates')],
    ```
    # file:settings.py
    TEMPLES = [
        {
            'BACKEND':'django.template.backends.django.DjangoTemplates',
            # 'DIRS':[],     
            'DIRS':[os.path.join(BASE_DIR,'templates')], # 添加模板路径
            'APP_DIRS':True,    # 是否索引各app里的templates目录
            ...
        },
    ]
    ```
* 模板的加载方式
    1. 通过loader获取模板，通过HttpResponse进行响应
        ```
         from django.template import loader
         # 1. 通过loader加载模板
         t = loader.get_template("模板文件名")
         # 2. 将t转换成HTML字符串
         html = t.render("字典数据")
         # 3. 用响应对象将转换的字符串返回给浏览器
         return HttpResponse(html)
        ```
    2. 通过render()直接加载并响应模板
        ```
        from django.shortcuts import render
        return render(request,'模板文件名',字典数据)
        ```
# Django模板语言
## 模板的传参
* 模板传参是指把数据形成字典，传参给模板，为模板渲染提供数据
1. 使用loader加载模板
    ```
    t = loader.get_template('xxx.html')
    html = t.render(字典数据)
    return HttpResponse(html)
    ```
2. 使用render加载模板
    ```
    return render(request,'xxx.html',字典数据)
    ```
## 模板的变量
1. 在模板中使用变量语法
    * {{变量名}}
    * {{变量名.index}}
    * {{变量名.key}}
    * {{对象.方法}}
    * {{函数名}}
    
    
    
