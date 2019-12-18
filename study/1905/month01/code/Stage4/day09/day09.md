# Day09 
## Day08回顾
### 控制台抓包  
打开方式及选项
```
1. 打开浏览器，F12打开控制台，找到Network选项卡
2. 控制台常用选项
    1. Network:抓取网络数据包
        1. ALL:抓取所有的网络数据包
        2. XHR:抓取异步加载的网络数据包
        3. JS抓取所有的JS文件
    2. Source:格式化输出并打断点调试JavaScript代码，有助于分析爬虫中一些参数
    3. Console:交互模式，可对JavaScript中的代码进行测试
3. 抓取具体网络数据包后
    1. 单击左侧网络数据包地址，进入数据包详情，查看右侧
    2. 右侧:
        1. Headers:整个请求信息
            General、Response Headers、Request Headers、Query String、 Form Data
        2. Preview:对响应内容进行预览
        3. Response:响应内容
```
## 有道翻译过程梳理
```
1. 打开首页
2. 准备抓包： F12控制台
3. 寻找地址
页面中输入翻译单词，控制台中抓取到网络数据包，查找并分析返回翻译数据的地址
4. 发现规律
找到返回具体数据的地址，在页面中多输入几个单词，找到对应的URL地址，分析对比Network - ALL(或者XHR) - Form Data,发现对应的规律
5. 寻找JS文件
右上角 ... -> Search -> 搜索关键字 -> 单击 -> 跳转到Sources,左下角格式化符号{}
6. 查看JS代码
    搜索关键字，找到相关加密方法
7. 断点调试
8. 完善程序   
```
## 增量爬取思路
```
1. 将爬取过的地址存放到数据库中
2. 程序爬取时先到数据库中进行比对，如果已经爬过，则不会继续爬取
```
## 动态加载网站数据抓取
```
1. F12打开控制台，页面动作抓取网络数据包
2. 抓取json问价URL地址
# 控制台 XHR :异步加载的数据包
# XHR -> Query String Parameters(查询参数)
```
## 数据抓取最终梳理
```
# 响应内容中存在
1. 确认抓取数据在响应内容中是否存在
2. 分析页面结构，观察URL地址规律
    1. 大体查看响应内容结构，查看是否有更改 -- (百度视频案例)
    2. 查看页面跳转URL地址变化，查看是否新跳转页面 -- (民政部案例)
3. 开始代码进行数据抓取

# 响应内容不存在
1. 确认抓取数据在响应中是否存在
2. F12抓包开始刷新页面或者执行某些行为，主要查看XHR异步加载数据包
    1. GET请求:Request Headers,Query String Paramters
    2. POST请求:Request Headers、FormData
3. 观察查询参数或者Form表单数据规律，如果需要进行进一步抓包分析处理
    1. 比如有道翻译的salt+sign，抓取并分析JS做进一步处理
    2. 此处注意请求头中的cookie和referer以及User-Agent
4. 使用res.json()获取数据，利用列表或者字典的方法获取所需数据
    # res.json()报错
    # json decode() error xxx xxx
    # 说明网站返回的根本就不是json数据，检查formdata或者QueryStringParamters
```
# Day09笔记
## 豆瓣电影数据抓取案例
* 目标
```
1. 地址:豆瓣电影 - 排行榜 -剧情
2. 目标:电影名称,电影评分
```
* 抓包(XHR)
```
1. Request URL(基准URL地址)
https://movie.douban.com/j/chart/top_list?
2. Query String(查询参数)
# 抓取的查询参数如下:
type: 11                # 电影类型
interval_id: 100:90     
action: ''              
start: 20               # 每次加载电影的起始索引值 0 20 40 60
limit: 20               # 每次加载的电影数量
```
* 代码实现-全站抓取-完美接口-指定类型所有电影信息
```
# F12抓到的地址
https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20
# 类型+类型码正则表达式
<a href="/typerank.*?type=(.*?)&.*?>(.*?)</a>
```
## 腾讯招聘数据抓取
* 确定URL地址及目标
```
1. 确定URL:百度搜索腾讯招聘 - 查看工作岗位
2. 目标:职位名称、工作职责、岗位需求
```
* 要求与分析
```
1. 通过查看网页源代码，得知所需数据均为Ajax动态加载
2. 通过F12抓取网络数据包，进行分析
3. 一级页面抓取数据:职位名称
4. 二级页面抓取数据:工作职责、岗位要求
```
* 一级页面json地址(index在变,itemstamp未检查)
```
https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576659970063&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn
```
* 二级页面地址(postId在变,在一级页面中可拿到)
```
https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1576660492144&postId={}&language=zh-cn
```
* 代码实现
```
# 一级页面
postId
# 二级页面
名称+职责+要求+发布时间+地点
```
## 多线程爬虫
**应用场景**
```
1. 多进程:CPU密集程序
2. 多线程:爬虫(网络I/O)、本地磁盘I/O
```
**知识点回顾**
* 队列
```
# 导入模块
from queue import Queue
# 使用
q = Queue()
q.put(url)
q.get() # 当队列为空时,阻塞
q.get(block=True,timeout=3)
q.get(block=False) # 为空时直接抛异常
q.empty() # 判断队列是否为空,True/False

```
* 线程模块
```
# 导入模块 
from threading import Thread
# 使用流程
t = Thread(target=函数名) # 创建线程对象
t.start() # 创建并启动线程
t.join()  # 阻塞等待回收线程
# 如何创建多线程???
t_list = []
for i in range(10):
    t = Thread(target=函数名)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()
```
```
from threading import Lock

lock = Lock()

n = 5000 

def f1():
    for i in range(2000):
        lock.acquire()
        n += 1
        lock.release()
def f2():
    for i in range(2000):
        lock.acquire()
        n -= 1
        lock.release()
t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()

# 计算机执行过程
n = n + 1
# +1操作
a = n + 1   a = 5000
a = n-1     a = 4999
n = a       n = 4999
n = a       n = 4999



```
## 小米应用商店抓取(多线程)
**目标**
```
1. 网址:百度搜索 - 小米应用商店,进入官网
2. 目标:所有应用分类
    应用名称
    应用链接
```
**实现步骤**
* 确认是否为动态加载
```
1. 页面局部刷新
2. 右键查看网页源代码，搜索关键字未搜到
# 此网站为动态加载网站，需要抓取网络数据包分析
```
* F12抓取网络数据包
```
1. 抓取返回json数据的URL地址(Headers中的Request URL)
    http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30
2. 查看并分析查询参数(headers中的QueryStringParameters)
    page: 0
    categoryId: 2
    pageSize: 30
    # 只有page在变,0,1,2...这样我们就可以通过page的值拼接多个返回json数据的URL地址
```
* 代码实现
```
# 类别
li_list = //ul[@class="category-list"]/li
name = li.xpath('./a/text()')
code = li.xpath('./a/@href')[0].split('/')[-1]
```


