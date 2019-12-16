# day04笔记
# Redis 事务
## 特点
```
1. 单独的隔离操作:事务中的所有命令会被序列化、按顺序执行，再执行过程中不会被其他客户端发送来的命令打断
2. 不保证原子性:redis中的一个事务中如果存在命令执行失败，那么其他命令会依然执行，没有回滚机制
```
## 事务命令
```
1. MULTI # 开启事务
2. 命令1 # 执行命令
3. 命令2 ... ...
4. EXEC # 提交到数据库执行
5. DISCARD # 取消事务
```
## 使用步骤
```
# 开启事务
127.0.0.1:3679> MULTI
OK
# 命令1入队列
127.0.0.1:3679> INCR n1
QUEUED
# 命令2入队列
127.0.0.1:3679> INCR n2
QUEUED
# 提交到数据库执行
127.0.0.1:3679> EXEC
1)(integer) 1
2)(integer) 2
```
## 事务中命令错误处理
```
# 1. 命令语法错误，命令入队失败，直接自动discard退出这个事务
    这个在命令在执行调用之前会发生错误。例如，这个命令可能有语法错误(错误的参数数量，错误的命令名)
    处理方案:客户端发生第一个错误情况，在exec执行之前发生的。通过检查队列命令返回值:如果这个命令回答这个队列的命令时正确的，否则redis会返回一个错误。如果那里发生了一个队列命令错误，大部分客户端将会推出并丢弃这个事务
# 2. 命令语法没错，但类型操作错误，则事务执行调用之后失败，无法进行事务回滚
    从我们施行了一个由于错误的value的key操作(例如对着string类型的value施行了List命令操作)
    处理方案:发生在EXEC之后的是没有特殊方式去处理的:即使某些命令在事务中失败，所有的其他命令都将会被执行。
127.0.0.1::3679> MULTI
OK
127.0.0.1:3679> set num 10
QUEUED
127.0.0.1:3679> LPOP num
QUEUED
127.0.0.1:3679> EXEC
1) OK
2) (error) WRONGTYPE Operation against a key holding thr wrong kind of value 
127.0.0.1:3679> get num
"10"
127.0.0.1:3679:>
```
## 为什么事务不支持回滚
* 观点
```
1. Redis的内部极其简单和快速，来源于它不需要回滚功能
2. 在生产环境中，通常回滚并不能解决来自编程的错误。举个例子，你本想+1,却+2了，又或者+在错误的类型上，回滚并不能解决。由于无法提供一个避免程序员自己的错误，而这种错误在产品中并不会出现，所以选择一个简单和快速的方法去支持事务
```
## pipeline补充
* python使用pipeline()与execute()批量操作进行批量操作
示例
```
import redis
# 创建连接池并连接到redis
pool = redis.ConnectionPool(host='127.0.0.1',db=0,port=6379)
r = redis.Redis(connection_pool=pool)
# 第一组
pipe = r.pipeline()
pip.set('fans',50)
pipe.incr('fans')
pipe.incrby('fans',100)
pipe.execute()
# 第二组
pipe.get('fans')
pipe.get('pwd')
# [b'151',b'123']
result = pipe.execute()
print(result)
```
## Redis常见问题汇总
* Redis优点
```
1. 读写速度快，数据存放在内存中
2. 支持数据类型丰富,string,hash,list,set,sorted
3. 支持事务
4. 可以用于缓存，消息队列，按key设置过期时间，到期后自动删除
5. 支持数据持久化(将内存数据持久化到磁盘)，支持AOF和RDB两种持久化方式，从而进行数据恢复工作，可以有效的防止数据丢失
6. 支持主从(master-slave)复制来实现数据备份，主机会自动将数据同步到从机
```
* 来介绍一下redis的数据类型

|类型|特点|使用场景|
|----|----|-------|
|string|简单key-value类型，value可为字符串和数字|常规计数(微博数，粉丝数等功能)|
|hash|是一个string类型的field和value的映射表，hash特别适合用于存储对象|存储部分可能需要变更的数据(比如用户信息)|
|list|有序可重复列表|关注列表，粉丝列表，消息队列等|
|set|无序不重复列表|存储并计算关系(如微博，关注人或粉丝存放在集合，可通过交集、并集、差集等操作实现如共同关注、共同喜好等功能)|
|sorted|每个元素带有分值的集合|各种排行榜|
* redis中的持久化方案
```
# RDB
    快照形式，定期内存中的数据保存到磁盘。Redis默认支持的持久化方案。速度快但是服务器断点的时候会丢失部分数据
# AOF 
    把所有对redis数据库增删改操作的命令保存到文件中。数据库恢复时把所有的命令执行一遍即可。
# 两种持久化方案同时开启使用AOF文件来恢复数据，能保证数据的完整性，但是速度慢。
```
* 使用过Redis分布式锁么，它是什么回事
```
1. 从redis2.8开始，set命令集成了两个参数，nx和ex,先拿nx来争抢锁，抢到之后，再用ex参数给锁加一个过期时间防止锁无法释放，造成死锁
2. redis分布式锁原理见图
# set donghaodong aaa nx ex 3
```
* 缓存穿透
```
# 原理
    缓存和数据库都没有的数据，而用户反复发起请求，如假的用户ID
# 场景
    比如发起为id为'-1'的数据或者id为特别大不存在的数据。这时的用户很可能是攻击者，攻击会导致数据库压力过大
# 解决方案
    1. 请求校验，接口层增加校验，如对id做基础校验，id<=0的直接拦截
    2. 都无法取到数据时也可以将key-value对写为key-null，缓存有效时间比如30秒左右，这样可以防止攻击用户反复同一个id暴力攻击
```
* 缓存击穿
```
# 原理
    缓存没有，数据库有，一般是缓存时间到期，顺势并发太大
# 解决方案
    1. 热点数据不过期
    2. 上锁:重新设计缓存的使用方式，当我们通过key去查询数据时，首先查询缓存，如果没有，就通过分布式锁进行加锁，取得锁的进程查DB并设置缓存，然后解锁；其他进程如果发现有锁就等待，然后等解锁后返回缓存数据或者再次查询DB
```
* 缓存雪崩
```
# 原理
    缓存中大批量数据过期，导致瞬时大批量不同请求注入DB
# 解决方案
    1. 缓存设置随机事件(避免缓存设置相近的有效期；为有效期增加随机值)
    2. 热点数据不过期
```
# 网络爬虫概述
## 定义
```
网络蜘蛛、网络机器人，抓取网络数据的程序
其实就是用Pyton程序模仿人点击浏览器并访问网站，而且模仿的越像越好，让web站点无法发现你不是人
```
## 爬取数据的目的
```
1. 公司项目测试数据
2. 公司业务部门及其他部门所需数据
3. 数据分析
```
## 企业获取数据方式
```
1. 公司自有数据
2. 第三方数据平台购买(数据堂、贵阳大数据交易所)
3. 爬虫爬取数据
```
## Python做爬虫优势
```
1. Python:请求模块、解析模块丰富成熟，强大的Scrapy网络爬虫框架
2. PHP:对多线程、异步支持不太好
3. Java:代码笨重，代码量大
4. C/C++:虽然效率高，但是代码成型慢
```
## 爬虫分类
```
1. 通用网络爬虫(搜索引擎使用，遵守robots协议)
    robots协议:网站通过robots协议告诉搜索引擎那些页面可以抓取，那些页面不能抓取，通用网络爬虫需要遵守robots协议(君子协议)
    http://www.taobao.com/robots.txt
2. 聚焦网络爬虫:自己写的爬虫程序
```
## 爬虫爬取数据步骤
```
1. 确定要爬取的URL地址
2. 由请求模块向URL地址发出请求，并得到网站的响应
3. 从响应内容中提取所需数据
    1. 所需数据，保存
    2. 页面中有其他需要继续跟进的URL地址，继续第二步去发请求，如此循环
```
# 爬虫请求模块一
## 模块名及导入
```
1. 模块名:urllib.request
2. 导入方式:
    1. import urllib.request
    2. from urllib import request
```
## 常用方法详解
### urllib.request.urlopen
* 作用
向网站发起请求并获取相应对象
* 参数
```
1. url:需要爬取的URL地址
2. timeout:设置等待超时时间，指定时间内未得到响应抛出超时异常
```
* 第一个爬虫程序-01_urlopen.py
打开浏览器,输入百度地址(http://www.baidu.com/),得到百度的响应
```
import urllib.request
# urlopen() : 向URL发请求，返回响应对象
response = urllib.request.urlopen('http://www.baidu.com/')
# 提取响应内容
html = response.read().decode('utf-8')
# 打印响应内容
print(html)
```
* 响应对象(response)方法
```
1. bytes = response.read() # read()得到结果为bytes数据类型
2. string = response.read().decode() # decode()转为string数据类型
3. url = response.geturl() # 返回实际数据的URL地址
4. code = response.getcode() # 返回HTTP响应码
# 补充
5. string.encode() # string -> bytes
6. bytes.decode() # bytes - > string
```
### 思考:网站如何判定是人类正常访问还是爬虫程序访问?
```
# 向测试网站:http://httpbin.org/get发请求，查看自己请求头 - 响应内容
# 代码如下
此处各位大佬自己完成
# html中的请求头header如下
"headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.7"
  }
发现请求头中user-Agent竟然是:Python-urllib/3.7!!!
我们需要重构User-Agent,发请求时带着User-Agent过去，但是urlopen()方法不支持重构User-Agent,那么我们怎么办？请看下面的方法!!
```
### url.request.Request
* 作用
创建请求对象(包装请求,重构User-Agent,使程序更像正常人类请求)
* 参数
```
1. url:请求的URL地址
2. headers:添加请求头(爬虫和反爬虫斗争的第一步骤)
```
* 使用流程
```
1. 构造请求对象(重构User-Agent)
    req = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"})
2. 发起请求获取相应对象(urlopen)
    res = urllib.request.urlopen(req)
3. 获取响应对象内容
    html = res.read().decode()
```
* 示例 - 03_Request.py
向测试网站(http://httpbin.org/get)发起请求，构造请求头并从响应中确认请求头信息
```
from urllib import request

# 定义变量
url = 'http://httpbin.org/get'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
# 1. 创建请求对象
req = request.Request(url=url,headers=headers)
# 2. 获取响应对象
res = request.urlopen(req)
# 3. 读取内容
html = res.read().decode()
print(html)
```
## URL地址编码模块
### 模块名及导入
* 模块
```
# 模块名
urllib.parse
# 导入
import urllib.parse
from urllib import parse
```
* 作用
给URL地址中查询参数进行编码
```
编码前:http://www.baidu.com/s?wd=美女
编码后:http://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
```
## 常用方法
### urllib.parse.urlencode({dict})
* URL地址中一个查询参数
```
# 查询参数:{'wd':'美女'}
# urlencode编码后:'wd=%e7%be%8e%e5%a5%b3'
# 示例代码
query_string = {'wd':'美女'}
result= urllib.parse.urlencode(query_string)
# result: 'wd=wd=%e7%be%8e%e5%a5%b3'
```
* URL地址中多个查询参数
```
from urllib import parse
query_string_set = {
    'wd':'美女',
    'pn':'50'
}
params = parse.urlencode(query_string_dict)
url = 'http://www.baidu.com/s?'{}.format(params)
print(url)
```
* 拼接URL地址的3种方式
```
# 1. 字符串相加
    baseurl = 'http://www.baidu.com/s?'
    params = 'wd=%e7%be%8e%e5%a5%b3'
    url = baseurl + params
# 2. 字符串格式化(占位符)
    params = 'wd=%e7%be%8e%e5%a5%b3'
    url = 'http://www.baidu.com/s?%s'%params
# 3. format()方法
    url = 'http://www.baidu.com/s?{}'
    params = 'wd=%e7%be%8e%e5%a5%b3'
    url = url.format(params)
```
* 练习
在百度中输入要搜索的内容，把响应内容保存到本地文件
```
请输入搜索内容:赵丽颖
# 最终保存到本地文件 - 赵丽颖.html
```
* 代码实现-04_parse_baidu.py
```
from urllib import request
from urllib import parse

# 1. 拼接url地址函数
def get_url(word):
    baseurl = 'http://www.baidu.com/s?'
    #编码+拼接
    params = parse.urlencode({'wd':word})
    url = baseurl + params
    return url
# 2. 请求+保存
def write_html(url,word):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    # 拿到响应内容
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 保存到本地文件
    filename = word + '.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

# 主程序入口
if __name__ == '__main__':
    word = input('请输入要搜索的内容:')
    url = get_url(word)
    write_html(url,word)
```
quote(string)编码
* 示例1



