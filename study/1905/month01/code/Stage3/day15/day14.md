# POST传递参数
* 客户端通过表单等POST请求将数据传递给服务器端，如：
```html
<form method="post" action="/login">
    姓名:<input type="text" name="username">
    <input type="submit" value="登录">
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
    request.POST['参数名']
    request.POST.get('参数名','')
    request.POST.getlist('参数名')
    ```
* 取消csrf验证，否则Django将会拒绝客户端发来的POST请求
    * 取消csrf验证
        * 删除settings.py中MIDDLEWARE中的CsrfViewsMiddleWare的中间件
        ```
        MIDDLEWARE = [
            '''
            # 'django.middleware.csrf.CsrfViewMiddleware',
            '''
        ]
        ```
# form表单的name属性

