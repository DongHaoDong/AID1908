# session会话控制
* 什么是session
* session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据
* session的起源
    * http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
    * 实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
    * 推荐使用session方式，所有数据存储在服务器端
* 实现方式
    * 使用session需要在浏览器客户端启动cookie,且用在cookie中存储sessionid
    * 每个客户端都可以在服务器端有一个独立的Session
    * 注意：不同的请求之间不会共享这个数据，与请求者一一对应
* Django启用Session
    * 在settings.py文件中
    * 向INSTALLED_APPS列表中添加
        ```
        INSTALL_APPS = [
            ...
            # 启用session应用
            'django.contrib.sessions',
        ]
        ```
    * 向MIDDLEWARE列表中添加:
        ```
        MIDDLEWARE = [
            # 启用session中间件
            
        ]
        ```
* session的基本操作
    * session对象是一个在类似于字典的SessionStore类型的对象，可以用类似与字典的方式进行操作
    * session只能够存储序列化的数据，如字典，列表等。
    1. 保存session的值到服务器
        * request.session['KEY'] = VALUE
    2. 获取session的值
        * VALUE = request.session['KEY']
        * VALUE = request.session.get('KEY',缺省值)
    * 删除session的值
        * del request.session['KEY']
    * 在settings.py中有关session的设置
        1. SESSION_COOKIE_AGE
            * 作用:指定sessionid在cookies中的保存时长(默认是两周),如下:
            * SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
        2. SESSION_EXPIRE_AT_BROWSER_CLOSE = True
            * 设置只要浏览器关闭时，session就失效(默认为False)
    * session缺省配置
        * 模块
            * import django.conf.global_settings
* 当使用session时需要迁移数据库，否则会出现错误
    ```
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```
# 用户登录逻辑处理
* 当用户登录时，可以在session添加一个键"user"绑定一个当前登录用户的信息，如果在'user' in request.session成立，即当前用户为登录状态，可以从request.session['user']获去登录信息。否则为没有登录状态
* 登录逻辑处理
    1. 检查用户和密码是否是合法用户
    2. 如果是合法用户，在当前用户的session记录
        ```
        # 在session内保存当前用的名称和id
        request.session['user'] = {
            'username':'tedu',
            'id':1
        }
        # 注：没有登录的用户request.session['user']不存在
        ```  
* 退出登录的逻辑处理
    3. 退出登录时，删除session['user']
        ```
        if 'user' in request.session:
            del request.session['user']
        ```
* 判断用户是否登录
    ```
    if 'user' in request.session:
        当前用户登录中
    else:
        没有用户登录
    ```
* 练习
    * 实现用户登录、退出功能
    * 说明
        * 如果用户输入的登录数据合法，则在session['user']内记录一个已经登录的用户状态
    * 要求:
        1. 创建一个user应用实现用户登录注册，退出登录的逻辑
            * python3 manage.py startapp user
        2. 创建一个index应用实现用户主页
            * python3 manage.py startapp index
    * 模型类
        1. 用户模型类
            ```
            class User(models.Model):
                username = models.CharField('用户名',max_length = 30, unique=True)
                password = models.CharField('密码',max_length = 30class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=30)

    def __str__(self):
        return "用户名" + self.username)
            ```
        2. 笔记模型类
            ```
            class Note(models.Model):
    title = models.CharField('标题',max_length=100)
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    mod_time = models.DateTimeField('修改时间',auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
            ```
            
            
                