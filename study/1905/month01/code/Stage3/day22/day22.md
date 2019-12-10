# AJAX
## 1. 什么是AJAX
Asynchronous Javascript And Xml
异步的 JS 和 xml(EXtensible Markup Language)
通过JS异步的向服务器发送请求并接收响应数据
* 同步访问
    * 当客户端向服务器发送请求时，服务器正在处理的过程中，浏览器只能等待，效率较低
* 异步访问
    * 当客户端向服务器发送请求时，服务器在处理的过程中，客户端可以做其他操作，不需要直接等待
* AJAX的优点
    1. 异步访问
    2. 局部刷新
* 使用场合
    1. 搜索建议
    2. 表单验证
    3. 前后端分离
## AJAX核心对象-异步对象(XMLHttpRequest)
1. 什么是XMLHttpRequest[简称xhr]
称为异步对象，代替浏览器向服务器发送异步的请求并接收响应
[xhr是由JS提供的]
2. 创建异步对象(xhr)
    1. IE7+,Chrome,Firefox,Safari,Opera ->调用XMLHttpRequest生成xhr对象
    2. IE低版本浏览器中(IE6以及以下)->调用ActiveXObject()生成xhr
    ```html
    <script >
        if(window.XMLHttpRequest){
            // 支持XMLHttpRequest
            var xhr = new XMLHttpRequest();
            
        }else{
            // 不支持XMLHttpRequest,使用ActiveXObject创建异步对象
            var xhr = new ActiveXObject('Microsoft.XMLHTTP');
        }
    </script>
    ```
3 xhr成员  
    1. 方法-open()  
        ```
        作用：创建请求
        语法：open(method,url,asyn)
        参数：
            method:请求方式，取值'get'或'post'
            url:请求地址，字符串
            asyn:是否采用异步的方式-true:异步/false:同步
        ex:xhr.open('get','/server',true);
        ```  
    2. 方法-send()
        ```
        作用:通知xhr向服务器发送请求
        语法:send(body)
        参数:
            get请求:body的值为null -> send(null)
            post请求:body的值为请求数据 -> send("请求数据")
        ```  
    3. 属性-readyState  
        ```
        作用:请求状态，通过不同的请求状态来表示xhr与服务器的交互情况  
        ```
        
|状态|说明|
|----|----|
|0|代理被创建,但尚未调用open()方法|
|1|open()方法已经被调用|
|2|send()方法已经被调用,响应头也已经被接收|
|3|下载中,responseText属性已经包含部分数据|
|4|下载操作已完成|
    4. 属性-responseText  
        ```
        作用:响应数据
        ```  
    5. 属性-status  
        ```
        作用:服务器端的响应状态码
        ```
        
|状态码|说明|
|------|---|
|200|表示服务器正确处理所有的请求以及给出响应|
|404|请求资源不存在|
|500|服务器内部错误|
    6. 事件-onreadystatechange
        ```
        作用:每当xhr的readState发生改变的时候都要触发的操作
        也称回调函数，当readState的值为4且status值为200的时候，才可以获取相应数据
        ```
## 3.AJAX的操作步骤
1. GET请求
```
// 1. 创建xhr请求
var xhr = createXhr()
// 2. 创建请求 - open()
xhr.open('get',url,asyn[true|false])
// 3. 设置回调函数 - onreadystatechange
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        // 接收响应
        xhr.responseText;
    }
}
// 4. 发送请求
xhr.send(null);
// 注意
```
2. POST请求
```
// 1. 创建xhr请求
var xhr = createXhr();
// 2. 创建请求 - open()
xhr.open('post',url,asyn[true|false])
// 3. 设置回调函数 -- onreadystatechange
xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        // 接收响应
        xhr.responseText;
    }
}
// 4. 设置Content-Type;
// 默认ajax post的Content-Type为"text/plain;charset=utf-8"
xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
// 5. 发送请求
xhr.send('请求数据')
// 请求数据同查询字符串 "username=donghaodong&age=21"
```
## JSON


            






    
 

    


