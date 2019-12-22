# Day14 
## Day13回顾
### settings.py常用变量
```
# 设置日志级别
LOG_LEVEL = ''
# 保存到日志文件(不在终端输出)
LOG_FILE = ''
# 设置数据导出编码(主要针对json文件)
FEED_EXPORT_ENCODING = ''
# 非结构胡数据存储路径
IMAGES_STORE = '路径'
# 设置User-Agent
USER_AGENT = ''
# 设置最大并发数(默认为16)
CONCURRENT_REQUESTS = 32
# 下载延迟时间(每隔多长时间请求一个网页)
DOWNLOAD_DELAY = 3
# 请求头
DEFAULT_REQUEST_HEADERS = {}
# 添加项目管道
ITEM_PIPELINES = {}
# 添加下载器中间件
DOWNLOADER_MIDDLEWARES = {} 
```
## 非结构化数据抓取
```
1. spider 
    yield item['连接']
2. pipelines.py
    from scrapy.pipelines.image import ImagesPipeline
    class TestPipeline(ImagesPipeline):
        def get_media_requests(self,item,info):
            yield scrapy.Request(url=item['url'],meta={'item':item['name']})
        def file_path(self,request,response=None,info=None):
            name = request.meta['item']
            filename = name
            return filename
3. settings.py
    IMAGES_STORE = 'D:\\Spider\\images'
```
## scrapy.Request()
```
1. url
2. callback
3. headers
4. meta:传递数据,定义代理
5. dont_filter:是否忽略组限制
默认False，检查allowed_domains['']
# request属性
request.url
request.headers
request.meta
request.method
# response.url
# response.text
# response.body
# response.meta
# response.encoding
```
## 设置中间件
### 随机User-Agent
```
# middlewares.py
class RandomUserAgentDownloaderMiddleware(object):
    def process_request(self,request,spider):
        request.header['User-Agent'] = xxx
# settings.py
DOWNLOADER_MIDDLEWARES = {
    'xxx.middlewares.xxx'"300
}
```
### 随机代理
```
# 1. middlewares.py
class RandomProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
        request.meta['proxy'] = xxx
    def process_exception(self,request,exception,spider):
        request request
# 2.settings.py
    DOWNLOADER_MIDDLEWARES = {'xxx.middlewares.xxx':200}
```
## item对象到底该在何处创建？
```
1. 一级页面:都可以，建议在for循环外
2. >=2二级页面: for循坏内
```
# Day11笔记
## 分布式爬虫
* 原理
```
多台主机共享一个爬虫队列 
```
* 实现
```
重写scrapy调度器(scrapy_redis模块)
```
* 为什么使用redis
```
1. Redis基于内存，速度快
2. Redis非关系型数据库,Redis中集合,存储每个request的指纹
3. scrapy_redis安装
    sudo pip3 install scrapy_redis
```
## scrapy_redis详解
* GitHub地址
```
http://github.com/rmax/scrapy-redis
```
* settings.py说明
```
#  重新指定调度器:请用Redis调度存储请求队列
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# 重新指定去重机制:确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# 不清除Redis队列:暂停/恢复/断点续爬
SCHEDULER_PERSIST = True
# 优先级队列(默认)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其他队列
# 先进先出队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# 后进先出队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
# redis管道
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':300
}
# 指定连接到redis时使用的端口和地址
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
```
## 腾讯招聘分布式改写
### 1. 正常项目数据抓取(分布式)
### 2. 改写为分布式(同时存入redis)
1. settings.py
```
# 1. 使用scrapy_redis调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# 2. 使用scrapy_redis去重机制
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# 3. 不清除请求指纹
SCHEDULER_PERSIST = True
# 4. 在ITEM_PIPELINES中添加redis管道
'scrapy_redis.pipelines.RedisPipeline':200,
# 5. 指定Redis的地址+端口号
REDIS_HOST = '192.168.43.220'
REDIS_PORT = 6379
```
### 2. 改写为分布式(同时存入mysql)
* 修改管道
```
ITEM_PIPELINES = {
    'Tencent.pipelines.TencentPipeline': 300,
    'Tencent.pipelines.TencentMysqlPipeline': 500,
    # 'scrapy_redis.pipelines.RedisPipeline':200,
}
```
* 清除redis数据库
```
flushdb
```
* 代码拷贝一份到分布式中其他机器,两台或多态机器同时执行此代码
**远程连接MySQL设置**
```
1. 配置文件 - 允许远程连接
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
# bind-address=127.0.0.1 把此行注释
2. 添加授权用户
mysql -u root -p123456
mysql> grant all privileges on *.* to '用户名'@'%' identified by '密码' with grant option;
mysql> flush privileges;
3. 重启MySQL服务
sudo /etc/init.d/mysql restart
```
## 腾讯招聘分布式改写-方法二
* 使用redis_key改写
```
# 第一步:settings.py无需改动和第一种写法一致
settings.py和上面分布式代码一致
# 第二步:tencent.py
from scrapy redis.spiders import RedisSpider
class TencentSpider(RedisSpider):
    # 1. 去掉start_urls
    # 2. 定义redis_key
    redis_key = 'tencent:spider'
    def parse(self,response):
        pass
# 第三步:把代码复制到所有爬虫服务器,并启动项目
# 第四步
    到redis命令行,执行LPUSH命令压入第一个需要爬取的URL地址
    > LPUSH tencent:spider 第一页的URL地址
# 项目爬取结束后无法退出，如何退出
settings.py
CLOSESPIDER_TIMEOUT = 3600
# 到指定时间(3600秒)时，会自动结束并退出
```
## scrapy-post请求
* 方法+参数
```
scrapy.FormRequest(
    url=posturl,
    formdata=formdata,
    callback=self.parse
)
```
* 有道翻译案例实现
1. 创建项目+爬虫文件 
```
scrapy startproject Youdao
cd Youdao
scrapy genspider youdao fanyi.youdao.com
```
2. item.py
```
result = scrapy.Field()
```
3. youdao.py
```
```
4. settings.py
```
1. ROBOTSTXT_OBEY = False
2. LOG_LEVEL = 'WARNING'
3. COOKIES_ENABLED = False
4. DEFAULT_REQUEST_HEADERS = {
    "Cookie": "OUTFOX_SEARCH_USER_ID=112756945@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=272803976.2557563; JSESSIONID=aaax-s4vw2NSRbSZ1NP8w; ___rl__test__cookies=1576951326355",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}
```
**scrapy添加cookie的三种方式**
```
# 1. 修改settings的三种方式
1. COOKIES_ENABLED = False 取消注释
2. DEFAULT_REQUEST_HEADERS = {} 添加cookie
# 2. DownloadMiddle
def process_request(self,request,spider):
    request.cookies={}
# 3. 爬虫文件
def start_request(self):
     yield scrapy.FormRequest(url=url,cookies={},callback=xxx)
```
## 机器视觉与tesseract
### 作用
```
处理图形验证码
```
### 三个重要概念
* OCR
```
# 定义
OCR:光学字符识别(Optical Character Recognition)
# 原理
通过扫描等光学输入方式将各种票据，报刊，书籍，文稿及其它印刷品的文字转化为图像信息，再利用文字识别技术将图像信息转化为电子文本
```
* tesseract-ocr
```
OCR的一个底层识别库(不是模块,不能导入)
# Google维护的开源OCR识别库
```
* pytesseract
```
Python模块，可调用底层识别库
# 对tesseract-ocr做的一层Python API封装
```
### 安装tesseract-ocr
* Ubuntu
```
sudo apt-get install tesseract-ocr
```
* Windows
```
1. 下载安装包
2. 添加环境变量(Path)
```
* 测试
```
# 终端 | cmd命令行
tesseract xxx.jpg 文件名
```
### 安装pytesseract
* 安装
```
sudo pip3 install pytesseract
```
* 使用
```
import pytesseract 
# Python图片处理标准库
from PIL import Image
# 创建图片对象
img = Image.open(test1.jpg)
# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)
```
* 爬取网站思路(验证码)
```
1. 获取验证码图片
2. 使用PIL库打开图片
3. 使用yytesseract将图片中识别码识别并转为字符串
4. 将字符串发送到验证码框中或者某个URL地址
```
## 在线打码平台
* 为什么使用在线打码
```
tesseract-ocr识别率很低、文字变形、干扰、导致无法识别验证码
```
* 云打码平台使用步骤
```
1. 下载并查看接口文档
2. 调整接口文档，调整代码并接入程序测试
3. 真正接入程序，在线识别后获取结果并使用
```
* 破解云打码网站验证码
1. 下载并调整接口文档,封装函数，打码获取结果
```
def get_result(filename):
    # 用户名
    username    = 'yibeizi001'
    # 密码
    password    = 'zhanshen002'
    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid       = 1
    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey      = '22cc5376925e9387a23cf797cb9ba745'
    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype    = 5000
    # 超时时间，秒
    timeout     = 60
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)
        # 登陆云打码
        uid = yundama.login();
        # 查询余额
        balance = yundama.balance();
        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
    return result
```
## Fiddler抓包工具
* 配置Fiddler
```
# 添加整数信任
1. Tools - options - HTTPS
    勾选Decrypt Https Traffic 后弹出窗口,一路确认
# 设置只抓取浏览器的数据包
2. ..from browser only
# 设置监听端口(默认为8888)
3. Tools - options - Connections
4. 关闭Fiddler,再打开Fiddler
```
* 配置浏览器代理
```
1. 安装Proxy Switchyomega插件
2. 浏览器右上角:SwitchyOmega->选项->新建情景模式->AID1908(名字)->创建
    输入:HTTP://127.0.0.1 8888
    点击:应用选项
3. 点击右上角SwitchyOmega可切换代理    
```
* Fiddler常用菜单
```
1. Inspector:查看数据包详细内容
    整体分为请求和响应两部分
2. 常用菜单
    Headers:请求头信息
    WebForms:POST请求Form表单数据:<body>
    GET请求查询参数:<QueryString>
    Raw
    将整个请求显示为纯文本
```
## 移动端app数据抓取
**方法1-手机+Fiddler**
```
设置方法见文件夹 - 移动端抓包配置
```
**方法2-F12浏览器工具**
**有道翻译手机版破解案例**
```

```
## 爬虫总结
```
# 什么是爬虫
    爬虫是请求网站并提取数据的自动化程序
# robots协议是什么
    爬虫协议或机器人协议,网站通过robots协议告诉浏览器引擎哪些页面可以抓取，哪些页面不能抓取
# 爬虫基本流程
    1. 请求得到响应
    2. 解析
    3. 保存数据
# 请求
    1. urllib
    2. requests
    3. scrapy
# 解析
    1. re正则表达式
    2. lxml+xpath解析
    3. json解析模块
# selenium+browser

# 常见的反爬策略
    1. Headers:最基本的反爬手段，一般被关注的变量是UserAgent和Referer,可以考虑使用浏览器中
    2. UA:建立User-Agent池,每次访问页面随机切换
    3. 拉黑高频访问IP
        数据量大用代理IP池伪造成多个访问者，也可控制爬取速度
    4. Cookies
        建立有效的cookie池,每次访问随机切换
    5. 验证码
        验证码数量较少可人工填写
        图形验证码可使用tesseract识别
        其他情况只能在线打码，人工打码和训练机器学习模型
    6. 动态生成
        一般由js动态生成的数据都是向特定的地址发get请求,返回的一般是json
    7. 签名及js加密
        一般为本地JS加密,查找本地JS文件,分析，或者使用execjs模块执行JS
    8. js调整页面结构
    9. js在响应中指向新的URL地址
# scrapy框架的运行机制

# 9. 分布式爬虫的原理
    多态主机共享一个爬虫队列
```



