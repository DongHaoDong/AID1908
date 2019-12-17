# Day07
## Day06回顾
## 目前反爬总结
* 基于User-Agent反爬
```
1. 发送请求携带请求头:headers={'User-Agent':'Mozilla/5.0 xxx'}
2. 多个请求随机切换User-Agent
    1. 定义列表存放大量User-Agent，使用random.choice()每次随机选择
    2. 定义py文件存放大量User-Agent,使用random.choice()每次随机选择
    3. 使用fake_useragent模块每次访问随机生成的User-Agent
        # sudo pip3 install fake_useragent
        * from fake_useragent import UserAgent
        * ua = UserAgent()
        * user_agent = ua.random
        * print(user_agent)
```
* 响应内容前端JS做处理反爬
```
1. html页面中可匹配出内容，程序中匹配结果为空
    * 响应内容中嵌入js,对页面结构做了一定调整导致，通过查看网页源码，格式化输出查看结构，更改xpath或者正则测试
2. 如果数据出不来可考虑更换IE的User-Agent尝试，数据返回最标准
```
## 请求模块总结
* urllib库使用流程
```
# 编码
params = {
    '':'',
    '':''
}
params = urllib.parse.urlencode(params)
url = baseurl + params
# 请求
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
```
* requests模块使用流程
```
params = {
    '':'',
    '':''
}
baseurl = 'http://tieba.baidu.com/f?'
html = requests.get(baseurl,params=params,headers=headers).content.decode('utf-8','ignore')
```
* 响应对象res属性
```
res.text:字符串
res.content:bytes
res.encoding:字符编码 res.encoding='utf-8'
res.status_code:HTTP响应码
res.url:实际数据URL地址
```
## 解析模块总结
* 正则解析re模块
```
import re
pattern = re.compile(r'正则表达式',re.S)
r_list = pattern.findall(html)
```
* lxml解析库
```
from lxml import etree
parse_html = etree.HTML(res.text)
r_list = parse_html.xpath('xpath表达式')
```
## xpath表达式
* 匹配规则
```
1. 节点列表
    # xpath示例
    //div、//div[@class="student"]、//div/a[@title="stu"]/span
2. 字符串列表
    # xpath表达式中末尾为：@src、@href、text()
```
* xpath高级
```
1. 基准xpath表达式:得到节点对象列表
2. for r in [节点对象列表]:
    username = r.xpath('./xxxx')
# 此处注意遍历后继续xpath一定要以:.开头，代表当前节点
```
## 写程序注意
```
# 最终目标:不要使你的程序因为任何异常而终止
1. 页面请求设置超时时间，并用try捕捉异常，超过指定次数则更换下一个URL地址
2. 所抓取任何数据，获取具体数据前先判断是否存在该数据，可使用列表推导式
# 多级页面数据抓取注意
1. 主线函数:解析一级页面函数(将所有数据从一级页面中解析并抓取)
```
## 增量爬虫如何实现
```
1. 数据库中创建指纹表，用来存储每个请求的指纹
2. 在抓取之前，先到指纹表中确认是否之前抓去过
```
## Chrome浏览器安装插件
* 安装方法
```
# 在线安装
1. 下载插件 - google访问助手
2. 安装插件 - google访问助手:chrome浏览器-设置-更多工具-扩展程序-开发者模式-拖拽(解压后的插件)
3. 在线安装其他插件 - 打开google访问助手 - google应用商店 - 搜索插件 - 添加即可
# 离线安装
1. 下载插件 - xxx.crx 重命名为 xxx.zip
2. 输入地址: chrome://extensions/ 打开-开发者模式
3. 拖拽插件(或者解压后文件夹)到浏览器中
4.  重启浏览器，使插件生效
```
# Day07笔记
## 链家二手房案例(xpath)
**实现步骤**
* 确认是否为静态
```
打开链家二手房页面 -> 查看网页源码 -> 搜索关键字
```
* xpath表达式
```
1. 基准xpath表达式(匹配每个房源信息节点列表)
    此处滚动鼠标滑轮时li节点的class属性会发生变化，通过查看网络源码确定xpath表达式
    //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]
2. 依次遍历后每个房源信息xpath表达式
    * 名称:'//div[@class="positionInfo"]/a[@class="no_resblock_a"]/text()'   
    # 户型+面积+方位+是否精装
    info_list = './/div[@class="houseInfo"]/text()'[0].strip().split('|')'
    * 户型:info_list[1]
    * 面积:info_list[2]
    * 方位:info_list[3]
    * 精装:info_list[4]
    * 楼层:info_list[5]
    * 区域:'.//div[@class="positionInfo"]/a/text()'
    * 总价:'.//div[@class="totalPrice"]/span/text()'
    * 单价:'.//div[@class="unitPrice"]/span/text()'
```
**代码实现**
```

```
