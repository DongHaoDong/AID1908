# JSON
## JSON介绍
JSON：JavaScript Object Notation  
在ajax中，循序将复杂格式的响应数据构建成JSON的格式再进行响应
## JSON表现
1. JSON表示单个对象
    1. 使用{}表示单个对象
    2. 在{}中使用key:value的形式来表示属性(数据)
    3. Key必须要用""引起来
    4. value如果是字符串的话，也需要用""引起来  
    js里的JSON对象->符合json规范的js对象就叫做json对象  
    JSON字符串->符合JSON规范的字符串
```
var obj = {
    "name":"王老师",
    "age":30,
    "gender":"Unknown"
}
```
## JSON表示一个数组
    1. 使用[]表示一个数组
    2. 数组中允许包含若干个JSON对象或字符串
        1. 使用JSON数组表示若干字符串
            ```
            var arr = ["王伟超","王夫人","王小超"];
            ```
        2. 使用JSON数组表示若干对象
            ```
            var arr = [
                {
                    "name":"王老师",
                    "age":30,
                    "gender":"男"
                },
                {
                    "name":"王夫人",
                    "age":31,
                    "gender":"女"
                }
            ];
            ```
## 使用jq的each()迭代数组
* 回顾JS中遍历数组
    ```
        var a = [{"name":"guoxiaonao","age":18},{"name":"weimingze""age":22}];
        for (var i=0;i<a.length;i++){
            var obj = a[i];
            console.log('name is'+obj.name);
            console.log('age is'+obj.age);
        }
    ```
1. $arr.each();
    ```
        // 语法:
        $arr.each(function(index,obj){
            index:遍历出来的元素下标
            obj:遍历出来的元素
        });
    ```
2. $.each()
    ```
        // 语法:
        $.each(arr,function(index,obj));
        arr: js中的普通数组
    ```
## 后台处理JSON
在后台查询出数据再转换为JSON格式的字符串，再响应给前端
1. 后台先获取数据
    * 类型允许为元组|列表|字典
2. 在后台将数据转换为符合JSON格式的字符串
3. 在后台将JSON格式的字符串进行响应
## Python中的JSON处理
```
import json
jsonStr = json.dumps(元组|列表|字典)
return jsonStr
```
Django中的JSON处理
```
# 方法1 使用Django中提供的序列化类来完成QuerySet到JSON
from django.core import serializers
json_str = serializers.serialize('json',QuerySet)
return HttpResponse(json_str)
# 方法2 
d = {'a':1}
return JsonResponse(d)
```
## 前端中的JSON处理
服务器端响应回来的数据是String,需要进行转换
```
JSON对象=JSON.parse(JSON字符串) // 反序列化
```
# Jquery对ajax的支持
1. $obj.load()
    * 作用:把指定的url的内容加载到指定的元素中
    * 语法
```
$obj.load(url,data,callback)
    $obj:显示内容的元素[jq对象]
    url:请求地址
    data:向url传入的参数[可选择]
        方式1
            查询字符串
            key=value&key1=value1...
            # 注意:用该方式传参,则为get请求
        方式2
            使用js对象/json对象
            {"name":"董浩东"}
            # 注意:用该方式传参，则为post请求
    callback:响应成功回调该函数[可选择]
```