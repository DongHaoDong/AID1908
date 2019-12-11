# JQuery对ajax的支持
## $obj.load()
* 作用:把指定的url的内容加载到指定的元素中
* 注意:当访问远程[跟当前域不一致的地址],浏览器将此次请求响应进行拦截
```
$obj.load(url,data,callback)
    $obj:显示内容的元素[jq对象]
    url:请求地址
    data:向url传入的参数[可选择]
        方式1：字符串传参
            "key1=value1&key2=value2"
            注意:用该方式传参,则为get请求
        方式2
            使用js对象/json对象
            {
                key1:"value1"，
                key2:"value2"
            }
            # 注意:用该方式传参，则为post请求
            默认不传参是get请求   
    callback:响应成功回调该函数[可选择]
```
注意：  
```
请求:
    GET请求:请求头无Content-Type
    POST请求:请求头一定有Content-Type
    $obj.load触发post时，ContentType为表弹头
    application/x-www-form-urlencoded
响应:
    响应头中一定会有Content-Type;具体内容具体分析
```
## $.get()和$.post()
* 作用:通过get方式异步的向远程地址发送请求
```
$.get(url,data,callback,type)
    url:请求地址
    data:传递到服务器端的参数
    可以是字符串:"name=sf.zh&age=18"
    也可以是js对象:
        {
            name:"zf.zh",
            age:18
        }
    callback:响应成功后的回调函数
    ex: function(data){
        console(data);
    }
    type:响应回来的数据的格式
    取值如下
        1.html:响应回来的文本是html文本
        2.text:响应回来的文本是text文本
        3.script:响应回来的文本是js执行脚本
        4.json:响应回来的文本是json格式的文本
```
## $.ajax()
```
参数对象中的属性
    1. url:字符串,表示异步请求的地址
    2. type:字符串，请求方式，get或post
    3. data:传递到服务器端的参数
        可以是字符串:"name=sf.zh&age=18"
        也可以是js对象
            {
                name:"sf.zh",
                age:18
            }
    4. dataType:字符串，响应回来的数据的格式
        1. 'html'
        2. 'xml'
        3. 'text'
        4. 'script'
        5. 'json'
        6. 'jsonp': 有关跨域的响应格式
    5. success:回调函数，请求和响应成功时回来执行的操作
    6. error:回调函数，请求或响应失败时回来执行的操作
    7. beforeSend:回调函数，发送ajax请求之前执行的操作,如果return false，终止请求
    8. async:是否为异步请求，true为异步请求，false为同步请求
```
## 跨域
### 什么是跨域
跨域:非同源的网页，相互发送请求的过程，就是跨域
```
浏览器的同源策略：
同源:多个地址中，相同协议，相同域名，相同端口被视为是"同源"
在HTTP中，必须是同源地址才能互相发送请求，非同源拒绝请求(<script>和<img>除外)
http://www.tedu.cn/a.html
http://www.tedu.cn/b.html
以上地址是"同源"

http://www.tedu.cn/a.html
https://www.tedu.cn/b.html
由于协议不同，所以不是"同源"

http://localhost/a.html
http://127.0.0.1/b.html
由于域名不同，所以不是"同源"

http://www.tedu.cn:80/a.html
http://127.0.0.1:8080/b.html
由于端口不同，所以不是"同源"
```
### 解决方案
通过script标签src向服务器资源发送请求
由服务器资源指定前端页面的哪个方法来执行响应的数据
### jquery跨域
jsonp - json with padding
用户传递一个callback参数给服务器端，然后服务器端返回数据时会将这个callback参数作为函数名来包裹住JSON数据
```
例如:
    当前地址:http://127.0.0.1:8000/index
    预访问地址:http://localhost:8000/data?callback=xxx
```
```
$.ajax({
    url:'xxx',
    type:'get',
    dataType:'jsonp',// 指定为跨域访问
    jsonp:'callback',// 定义了callback的参数名,以便于获取callback传递过去的函数名
    jsonpCallback:'xxx'// 定义jsonp的回调函数名
});

// 超简版本
$.ajax({
    url:'xxx',
    type:'get',
    dataType:'jsonp',// 指定为跨域访问
    success:function(data){
        console.log(data);
    }
});
```



