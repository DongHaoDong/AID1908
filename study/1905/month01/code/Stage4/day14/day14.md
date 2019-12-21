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

        
```