# 前后端分离
## 什么是前后端分离
前端：即客户端，负责渲染用户显示界面(如web的js动态渲染页面，安卓，IOS，pc客户端等)  
后端：即服务器端，负责接收http请求，处理数据  
API：Application Programming Interface是一些预先定的函数，或指软件系统不同组成部分衔接的约定  
前后端分离完整请求过程  
1. 前端通过http请求后端API  
2. 后端以json形式返回前端数据  
3. 前端生成用户显示界面[如html,ios,android]
### 判断前后端分离的核心标准：谁生成显示页面
1. 后端生成[前后端未分离]ex:flask->render_template django->HttpResponse(html)/render  
2. 前端生成[前后端分离]
return HttpResponse(json_str)
## 优点
1. 各司其职
前端：视觉层面，兼容性，前端性能优化
后端：并发，可用性，性能
2. 解耦，前端和后端均易于扩展
3. 后端灵活搭配各类前端-如安卓等
4. 提高用户体验
5. 前端+后端可以完全并行开发，加快开发效率
## 分离常见问题
|问题|答案|
|----|----|
|如何解决http无状态|采用token(详情见下方章节)|
|如果前端为JS，如何解决跨域问题|采用CORS(详情见下方章节)|
|如何解决csrf问题|采用token|
|Single Page Web Application是否会影响Search Engine Optimization效果|会，前后端分离后，往往页面不存在静态文字[例如新闻的详情内容]|
|"老板，这个逻辑到底是让前端做还是后端做啊?"|底线原则：数据校验需要前后端都做|
|"老板，前端工作压力太大了啊"|团队谢罪哦不能只是嘴上说说|
|动静分离和前后端分离是一个意思吗?|动静分离指的是css/js/img这类静态资源跟服务器拆开部署，典型方案-静态资源交由CDN厂商处理|
## 实现方式
1. Django/Flask后端只返回json
2. 前端->ex:js向服务器发送ajax请求，获取数据，拿到数据后动态生成html
3. 前端服务和后端服务分开部署
# token-令牌
## 学前须知
1. base64"防君子不防小人"  

|方法|作用|参数|
|----|---|----|
|b64encode|将输入的参数转化为base64规则|预加密的明文，类型为bases,例：b'guoxiaonao'|
|b64decode|将base64串解密回明文|base64密文，类型bases;例：b'Z3VveGIhb25hbw=:|
|urlsafe_64encode|作用同b64encode但是会将'+'替换成'-',将'/'替换成'_'|同b64encode|
|urlsafe_b64decode|作用同b64decode|同b64decode|
代码演示
```
import base64
# base64加密
s = b'guoxiaonao'
b_s=base64.b64encode(s)
# b_s打印结果为b'Z3VveGlhb25hbw=='
# base64解密
ss = base64.b64decode(b_s)
## ss打印结果为b'guoxiaonao'
```
2. SHA-256安全散列算法的一种(hash)
hash三大特点  
    * 定长输出 
    * 不可逆 
    * 雪崩
```
import hashlib
s = hashlib.sha256() # 创建sha256对象
s.update(b'xxxx') # 添加欲hash的内容,类型为bytes
s.digest() # 获取最终结果
```
3. HMAC-SHA256是一种通过特别计算方式之后产生的消息认证码，使用散列算法同时结合一个加密秘钥。它可以用来保证数据的完整性，同时可以用来做某个消息的身份验证
```
import hmac
# 生成一个hmac对象
# 第一个参数为加密的key,bytes类型
# 第二个参数为欲机密的串，bytes类型
# 第三个参数为hmac的算法，指定为SHA256
h = hmac.new(key,str,digestmod='SHA256')
h.digest() # 获取最终结果
```
4. RSA256非对称加密
    1. 加密:公钥加密，私钥解密
    2. 签名:私钥签名，公钥验签
# JWT-json-web-token
## 三大组成
1. header  
格式为字典-元数据格式如下
```
{'alg':'HS256','typ':'JWT'}
# alg代表要使用的算法
# typ代表该token的类别-此处必须为大写的JWT
```
该部分数据需要转成json串并用base64加密  
2. payload  
格式为字典-此部分分为共有声明和私有声明  
* 公共声明:JWT提供了内置关键字用于描述常见的问题此部分均为可选项，用户根据自己需求按需添加key,常见公共声明如下:
```
{'exp':xxx, # Expiration Time 此token的过期时间的时间戳
 'iss':xxx, # (Issuer) Claim 指明token的签发者
 'iat':xxx, # (Issued At) Claim 指明此token创建时间的时间戳
 'aud':xxx, # (Audience) Claim 指明此token签发面向群体
}
```
* 私有声明:用户可以根据自己的业务需求，添加自定义的key,例如下:
```
{'username':'guoxiaonao'}
```
公共声明和私有声明均在同一个字典中，转成json串并用base64加密
3. signature签名  
签名规则如下：  
根据header中的alg确定具体算法，一下用HS256为例  
HS256(自定义的key,base64后的header+'.'+base64后的payload)  
解释：用自定义的key,对base64后的header+'.'+base64后的payload进行hmac计算
## jwt结果格式
base64(header)+'.'+base64(payload)+'.'+base64(sign)  
最终结果如下： 
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1b3hpYW9uYW8iLCJpc3MiOiJnZ2cifQ.Zzg1u55DCBqPRGf9z3-NAn4kbA-MJN83SxyLFfc5mmM'
## 校验jwt规则
1. 解析header,确认alg
2. 签名校验，根据传过来的header和payload按alg指明的算法进行签名，将签名结果和传过来的sign进行对比，若对比一致，则校验通过
3. 获取payload自定义内容








