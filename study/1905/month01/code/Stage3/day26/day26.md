# pyjwt
1. 安装pyjwt
    * pip3 install pyjwt

|方法|参数说明|返回值|
|----|-------|-----|
|encode(payload,key,algorithm)|paload：jwt三大组成中的payload，需要组成字典，按需添加共有声明和私有声明，例如：{'username':'donghaodong','exp':584023982}参数类型dict|token串返回类型：bytes|
||key：自定义的加密key参数类型：str||
||algorithm：需要使用的加密算法[AHS256,RSA256等]，参数类型：str||
|decode(token,key,algorithm)|token：token串，参数类型：bytes/str|payload明文 返回类型：dict|
||key：自定义的加密key，需要跟encode中的key保持一致参数类型：str||
||algorithm：同encode||
||issuer：发布者,若encode payload中添加'iss'字段，则可针对该字段校验,参数类型str|若iss校验失败，则抛出jwt.InvalidIssuerError|
||audience：签发的受众群体，若encode payload中添加'aud'字段，则可针对该字段校验，参数类型：str|若aud校验失败，则抛出jwt.InvalidAudienceError|
PS：若encode的时候payload中添加了exp字段；则exp字段的值需为当前时间戳+此token的有效时间，例如希望token300秒后过期{'exp':time.time()+300};在执行decode时，若检查exp字段，且token过期，则抛出jwt.ExpiredSignatureError
# CORS-Cross-origin resource sharing-跨域资源共享
## 什么是CORS
允许浏览器向跨源(协议+域名+端口)服务器，发出XMLHttpRequest请求，从而克服了Ajax只能同源使用的限制
## 特点
* 浏览器自动完成(在请求头中加入特殊头或发送特殊需求)
* 服务器需要支持(响应头中需要有特殊头)
## 简单请求(Simple requests)和预检请求(Preflighted requests)
* 满足一下全部条件的请求为简单请求
    1. 请求方法如下:
         * GET or HEAD or POST
    2. 请求头仅包含如下:
        * Accept
        * Accept-Language
        * Content-Language
        * Content-Type
    3. ContentType仅支持如下三种:
        * application/x-www-form-urlencoded
        * multipart/form-data
        * text/plain
* 不满足以上任意一点的请求都是预检请求
# 简单请求发送流程
1. 请求
    * 请求中携带Origin,该字段表名自己来自哪个域
2. 响应
    * 如果请求头重的Origin在服务器接受范围内，则返回如下头

    |响应头|作用|备注|
    |-----|----|----|
    |Accept-Control-Allow-Origin|服务器接受的域||
    |Accept-Control-Allow-Credentials|是否接受Cookie|可选|
    |Access-Control-Expose-Headers|默认情况下，xhr只能拿到如下响应头：Cache-Control,Content-Language,Content-Type,Expires,Last-Modified;如果有需要获取其他头，需要在此指定|可选|  
    
    * 如果服务器不接受此域，则响应头中不包含Access-Control-Allow-Origin
# 预检请求发送流程
1. OPTION请求发起，携带如下请求头

    |请求头|作用|备注|
    |-----|----|----|
    |Origin|表明此请求来自哪个域|必选|
    |Access-Control-Request-Method|此次请求使用的方法|必选|
    |Access-Control-Request-Headers|此次请求使用的头|必选|
2. OPTION接受响应阶段，携带如下响应头
    
    |响应头|作用|备注|
    |-----|----|----|
    |Access-Control-Allow-Origin|同简单请求|必选|
    |Access-Control-Allow-Methods|告诉浏览器，服务器接受的跨域请求方法|必选|
    |Access-Control-Allow-Header|返回所有支持的头部，当request有Access-Control-Request-Headers时，该响应头必然回复|必选|
    |Access-Control-Allow-Credentials|同简单请求|可选|
    |Access-Control-Max-Age|OPTION请求缓存时间单位s|可选|
3. 主请求阶段

    |请求头|作用|备注|
    |-----|----|----|
    |Origin|表明此请求来自哪个域||
4. 主请求响应阶段

    |响应头|作用|备注|
    |-----|----|----|
    |Access-Control-Allow-Origin|当前服务器接受的域||
# Django支持
* django-cors-headers官网https://pypi.org/project/django-cors-headers/
直接pip将django升级到2.0一行，强烈建议用离线安装方式  
配置流程  
```
1. INSTALLED_APPS中添加corsheaders
2. MIDDLEWARE中添加
corsheaders.middleware.CorsMiddleware
3. CORS_ORIGIN_ALLOW_ALL布尔值如果为True，白名单不启用
4. CORS_ORIGIN_WHITELIST = [
    "http://example.com"
]
5. CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
6. CORS_ALLOW_HEADERS = (
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
7. CORS_PREFILGHT_MAX_AGE 默认 86400s
8. CORS_EXPOSE_HEADERS []
9. CORS_ALLOW_CREDENTIALS 布尔值，默认False
```
# RESTful-Representational State Transfer
## 什么是RESTful
1. 资源(Resources)  
网络上的一个实体或者说是网络上的一个具体信息，并且每个资源都有一个独一无二的URL与之对应，获取资源直接访问URL即可
2. 表现层(Representation)  
如何去表现资源 - 即资源的表现形式；如HTML，xml,JPG,json等
3. 状态转化(State Transfer)  
访问一个URL即发生了一次客户端和服务端的交互，此次交互将会涉及到数据和状态的变化  
客户端需要通过某些方式触发具体的变化-HTTP method 如 GET,POST,PUT,PATCH,DELETE等  
## RESTful的特征
1. 每个URL代表一种资源
2. 客户端和服务器端之间传递着资源的某种表现
3. 客户端通过HTTP的几个动作对资源进行操作-发生状态转化
## 如何设计符合RESTful特征的API
1. 协议 - http/https
2. 域名  
域名中体现出api字样，如  
https://api.example.com  
or  
https://example.org/api/  
3. 版本  
https://api.example.com/v1/  
4. 路径  
路径中避免使用动词，资源用名次表示，案例如下  
```
https://api.example.com/v1/users
https://api.example.com/v1/animals
```
5. HTTP动词语义
* GET(SELECT):从服务器取出资源(一项或多项)
* POST(CREATE):在服务器新建一个资源
* PUT(UPDATE):在服务器更新资源(客户端提供改变后的完整资源)
* PATCH(UPDATE):在服务器跟新资源(客户端提供改变的属性)
* DELETE(DELETE):从服务器删除资源
具体案例如下:
```
GET /zoos:列出所有动物园
POST /zoos:新建一个动物园
GET /zoos/ID:获取某个指定动物园的信息
PUT /zoos/ID:更新某个指定动物园的信息(提供该动物园的全部信息)
PATCH /zoos/ID:更新某个指定动物园的信息(提供该动物园的部分信息)
DELETE /zoos/ID:删除某个动物园
GET /zoos/ID/animals:列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID:删除某个指定动物园的指定动物
```
6. 巧用查询字符串
```
?limit=10:指定返回记录的数量
?offset=10:指定返回记录的开始位置
?page=2&per_page=100:指定第几页，以及每页的记录数
?sortby=name&order=asc:指定返回结果按照哪个属性排序，以及排序顺序
?type_id=1:指定筛选条件
```
7. 状态码
    1. 用HTTP响应码表达此次请求结果，例如
    ```
    200 ok - [GET]:服务器成功返回用户请求的数据
    201 CREATED - [POST/PUT/PATCH]:用户新建或修改数成功
    202 Accepted- [*]:表示一个请求已经进入后台排队(异步任务)
    204 Not CONTENT - [DELETE]:用户删除数据成功
    400 INVALID REQUEST - [POST/PUT/PATCH]:用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的
    401 Unauthorized - [*]:表示用户没有权限(令牌、用户名、密码错误)
    403 Forbidden - [*]:表示用户得到授权(与401错误相对)，但是访问是被禁止的
    404 Not FOUND - [*]:用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的
    406 Not Acceptable - [GET]:用户请求的格式不可得(比如用户请求JSON格式，但是只有XML格式)
    410 Gone - [GET]:用户请求的资源被永久删除，且不会再得到的
    422 Unprocessable entity - [POST/PUT/PATCH]:当创建一个对象时，发生一个验证错误
    500 INTERNAL SERVER ERROR - [*]:服务器发生错误
    ``` 
    2. 自定义内部code进行响应  
    如返回结构如下{'code':200,'data':{},'error':'返回信息'}
8. 返回结果  
根据HTTP动作的不同，返回结果的机构也有所不同  
```
GET /users:返回资源对象的列表(数组)
GET /users/guoxiaonao:返回单个资源对象
POST /users:返回新生成的资源对象
PUT /users/guoxiaonao:返回完整的资源对象
PATCH /users/guoxiaonao:返回完整的资源对象
DELETE /users/guoxiaonao:返回一个空文档
```










    

       



