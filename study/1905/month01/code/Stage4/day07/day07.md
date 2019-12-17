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
'''
链家房源信息爬取
'''
import requests
from lxml import etree
from fake_useragent import UserAgent
import random
import time


class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://xa.lianjia.com/ershoufang/pg{}/'

    # 功能函数1:获取随机User-Agent
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    # 获取页面函数
    def get_html(self,url):
        # 设置超时时间5秒钟，尝试次数3次
        for i in range(3):
            try:
                res = requests.get(url=url,headers=self.get_headers(),timeout=5)
                res.encoding = 'utf-8'
                html = res.text
                return html
            except Exception as e:
                continue

    # 解析页面
    def parse_html(self,url):
        # html返回值两种:1-html 2-None
        html = self.get_html(url)
        if html:
            parse_obj = etree.HTML(html)
            # 1.解析基准xpth:li节点对象列表
            li_list = parse_obj.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            # 2. for循环依次遍历每个li节点，获取1个房源所有数据
            item = {}
            for li in li_list:
                # 名称
                re_bds = '//div[@class="positionInfo"]/a[@class="no_resblock_a"]/text()'
                name_list = li.xpath(re_bds)
                item['name'] = [name_list[0].strip() if name_list else None][0]
                # 户型+面积+方位+精装
                # info_list:['','三室两厅','100.99平米','南北','精装']
                re_bds = './/div[@class="houseInfo"]/text()'
                info_list = li.xpath(re_bds)
                info_list = [info_list[0].split('|') if info_list else None][0]
                if len(info_list) == 6:
                    item['model'] = info_list[0].strip()
                    item['area'] = info_list[1].strip()[:-2]
                    item['direction'] = info_list[2].strip()
                    item['prefect'] = info_list[3].strip()
                    item['floor'] = info_list[4].strip()
                else:
                    item['model'] = item['area'] = item['direction'] = item['prefect'] = item['floor'] = None

                # 楼层+地区+总价+单价
                item['address'] = li.xpath('.//div[@class="positionInfo"]/a/text()')[0].strip()
                item['total'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
                item['unit'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()[2:-4]
                print(item)

    def run(self):
        for pg in range(1,101):
            url = self.url.format(pg)
            self.parse_html(url)
            time.sleep(random.randint(1,3))

if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.run()
```
## 百度贴吧图片爬取
* 目标
```
抓取指定贴吧所有图片
```
* 思路
```
1. 获取贴吧主页URL，下一页，找到不同页的URL规律
2. 获取1页中所有帖子URL地址:[帖子链接1,'帖子链接2,...']
3. 对每个帖子链接发请求，获取图片URL
4. 向图片的URL发请求，以wb方式写入本地文件
```
### 实现步骤
* 贴吧URL规律
```
http://tieba.baidu.com/f?kw=??&pn=50
```
* xpath表达式
```
1. 帖子链接xpath
    写法1： //div[@class='ton clearfix']/div/div/div/a/@href
    写法2： //li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href
2. 图片链接xpath
    //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src
3. 视频链接xpath
    //div[@class="video_src_wrapper"]/embed/@data-video
```
**代码实现**
```
# 一级页面:提取帖子链接
# 对每个帖子链接发请求
# 响应提取图片链接请求
# 保存图片
```
## requests.get()参数
### 查询参数-params
* 参数类型
```
字典，字典中键值对作为查询参数
```
* 使用方法
```
1. res = requests.get(url,params=params,headers=headers)
2. 特点:
    * url为基准的url地址，不包含查询参数
    * 该方法会自动对params字典编码，然后和url拼接
```
* 示例
```
import requests
baseurl = 'http://tieba.baidu.com/f?'
params = {
    'kw':'赵丽颖吧',
    'pn':'50'
}
headers = {'User-Agent':'Mozilla/4.0'}
# 自动对params进行编码，然后自动和url进行拼接，去发请求
res = requests.get(url=baseurl,params=params,headers=headers)
res.encoding = 'utf-8'
print(res.text)
```
**练习-修改百度贴吧案例为params参数**
```
from urllib import parse

import requests
from lxml import etree
import time
import random


class TiebaImageSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    # 功能函数1:获取html
    def get_html(self,url,params={}):
        res = requests.get(url=url,params=params,headers=self.headers)
        html = res.content
        return html

    # 功能函数2:解析
    def xpath_func(self,html,xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)
        return r_list

    # 做事情
    def parse_html(self,url,params):
        # 1. 提取帖子链接
        one_html = self.get_html(url,params).decode()
        xpath_bds = '//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href'
        # tlink_list: ['/html/xxx','','']
        tlink_list = self.xpath_func(one_html,xpath_bds)
        print(tlink_list)
        # 2. for遍历
        for tlink in tlink_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # 对1个帖子链接做完所有事情
            # 向帖子发请求+提取图片链接+向图片链接发请求+保存图片
            self.get_image(tlink)

    # 向帖子发请求+提取图片链接+向图片链接发请求+保存图片
    def get_image(self,tlink):
        html = self.get_html(tlink).decode()
        xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        image_link_list = self.xpath_func(html,xpath_bds)
        print(image_link_list)
        for img_link in image_link_list:
            # 保存图片
            self.save_image(img_link)

    # 保存图片
    def save_image(self,img_link):
        html = self.get_html(img_link)
        filename = img_link[-10:]
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    # 入口函数
    def run(self):
        name = input("请输入贴吧名:")
        start = int(input('起始页:'))
        end = int(input("终止页:"))
        for page in range(start,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.parse_html(self.url,params)

if __name__ == "__main__":
    spider = TiebaImageSpider()
    spider.run()

```
## Web客户端验证参数-auth
* 作用及类型
```
1. 针对于需要web客户端用户名密码认证的网站
2. auth = ('username','password')
```
* 达内code课程方向案例
```
# xpath表达式
//a/@href
# url
http://code.tarena.com.cn/AIDCode/aid1907/13-Redis/
```
* 思考爬取具体的笔记文件
```
import requests
from lxml import etree
from fake_useragent import UserAgent
import os


class CodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1907/13-Redis/'
        self.auth = ('tarenacode','code_2013')

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    def parse_html(self):
        # 1. 获取响应
        html = requests.get(
            url=self.url,
            auth=self.auth,
            headers=self.get_headers()
        ).text
        # 2. 解析响应内容
        parse_obj = etree.HTML(html)
        href_list = parse_obj.xpath('//a/@href')
        # 只提取.zip|.rar|.tar.gz的文件
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar') or href.endswith('.tar.gz'):
                self.save_file(href)

    def save_file(self,href):
        base_directory = 'D:/'
        directory = base_directory + '/'.join(self.url.split('/')[3:-1]) + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 下载链接
        file_url = self.url + href
        html = requests.get(
            url=file_url,
            auth=self.auth,
            headers=self.get_headers()
        ).content
        filename = directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print(href,'下载成功')

    def run(self):
        self.parse_html()


if __name__ == "__main__":
    spider = CodeSpider()
    spider.run()
```
## SSL证书认证参数-verify
* 使用网站及场景
```
1. 适用网站:https类型网站但是没有经过证书认证机构认证的网站
2. 适用场景:抛出SSLError异常则考虑使用此函数
```
* 参数类型
```
1. verify=True(默认):检查证书认证
2. verify=False(常用):忽略证书认证
# 示例
response = requests.get(
    url=url,
    params=params,
    headers=headers,
    verify=False
)
```
## 代理参数-proxies
* 定义
```
1. 定义:代替你原来的IP地址去对接网络的IP地址。
2. 作用:隐藏自身真实IP,避免被封。
```
**普通代理**
* 获取代理IP网站
```
西祠代理、快代理、全网代理、代理精灵...
```
* 参数类型
```
1. 语法结构
    proxies = {
        '协议':'协议://IP:端口号'
    }
2. 示例
    proxies = {
        'http':'http://IP:端口号',
        'https':'https://IP:端口号'
    }
```
* 示例
使用免费普通代理IP访问测试网站：http://httpbin.org/get
```
import requests
url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
# 定义代理，在代理IP网站中查找免费代理IP
proxies = {
    'http':'http://183.167.217.152:63000',
    'https':'https://183.167.217.152:63000'
}
html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)
```
**思考建立一个自己的代理IP池,随时更新用来抓取网站数据**
```
1. 从西刺代理IP网站上 ，抓取免费代理IP
2. 测试抓取的IP，可用的保存在文件中
```
**思考-代码实现**
```

```
写一个获取收费开放代理的接口
```
```
**私密代理**

- **语法格式**

```
1、语法结构
proxies = {
    '协议':'协议://用户名:密码@IP:端口号'
}

2、示例
proxies = {
	'http':'http://用户名:密码@IP:端口号',
  'https':'https://用户名:密码@IP:端口号'
}
```

**示例代码**

```python
import requests
url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://309435365:szayclhp@106.75.71.140:16816',
    'https':'https://309435365:szayclhp@106.75.71.140:16816',
}
headers = {
    'User-Agent' : 'Mozilla/5.0',
}

html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)
```

## **今日作业**

```
1、总结前几天内容,理顺知识点
2、代理参数 - 如何建立自己的IP代理池,并使用随机代理IP访问网站
3、Web客户端验证 - 如何下载、保存
```
