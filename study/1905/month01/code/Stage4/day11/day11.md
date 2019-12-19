# Day11
## Day10回顾
### cookie模拟登陆
```
1. 适用网站类型:爬取网站页面时需要登录后才能访问，否则获取不到页面的实际响应数据
2. 方法1(利用cookie)
    1. 先登录成功1次,获取到携带登录信息的Cookie(处理headers)
    2. 利用处理的headers向URL地址发请求
3. 方法2(利用处理的headers.get()中的cookies)
    1. 先登录成功1次，获取到cookie处理为字典
    2. res=requests.get(xxx,cookies=cookies)
4. 方法3(利用session会话保持)
    1. 实例化session对象
        session = requests.session()
    2. 先post:
    session.post(post_url,data=data,headers=headers)
        1. 登陆:找到POST地址:form -> action对应的url
        2. 定义字典，创建session实例化发送请求
            # 字典key : <input>标签中name的值(email,password)
            # post_data = {'email':'','password',''}
    3. 再get
    session.get(url,headers=headers)
```
### 三个池子
```
1. User-Agent
2. 代理池
3. cookie池
```
### selenium+phantomjs/chrome/firefox
* 特点
```
1. 简单，无需去详细抓取分析网络数据包，使用真实浏览器
2. 需要等待页面元素加载,需要时间,效率低
```
* 安装
```
1. 下载、解压
2. 添加到系统环境变量
    # windows:拷贝到Python安装目录的Script目录中
    # Linux:拷贝到/usr/bin目录中
3. Linux修改权限
    # sudo i
    # cd /usr/bin/
    # chmod +x phantomjs
        修改权限前:rwxr--r--
        修改权限后:rwxr-xr-x
```
* 使用流程
```
from selenium import webdriver
# 创建浏览器对象
browser = webdriver.Firefox(executable_path='/xxx/geckodriver')
# 2. 输入网址
browser.get('URL')
# 3. 查看节点
browser.find__xxx
# 4. 做对应操作
element.send_keys('')
element.click()
# 5. 关闭浏览器
browser.quit()
```
* 重要知识点
```
1. browser.page_source
2. browser.page_source.find('')
3. node.send_keys('')
4. node.click()
5. find_element AND find_elements
6. browser.execute_script('javascript')
7. browser.quit()
```
# Day11笔记
## chromedriver设置无界面模式
```
from selenium import webdriver
options = webdriver.ChromeOptions()
# 添加无界面参数
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.jpg')
```
## selenium - 键盘操作
```
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 搜索框中输入"selenium"
browser.find_element_by_id('kw').send_keys('赵丽颖')
# 输入空格
browser.find_element_by_id('kw').send_keys(keys.SPACE)
# Ctrl+a全选
browser.find_element_by_id('kw').send_keys(keys.CONTROL,'a')
# 4. Ctrl + c 模拟复制
browser.find_element_by_id('kw').send_keys(keys.CONTROL,'c')
# 5. Ctrl + v 模拟粘贴
browser.find_element_by_id('kw').send_keys(keys.CONTROL,'v')
# 6. 输入回车,代替搜索按钮
browser.find_element_by_id('kw').send_keys(keys.ENTER)
```
## selenium - 鼠标操作
```
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
# 移动到设置,perform()是真正执行操作,必须有
element = driver.find_element_by_xpath('//*[@id="ul"]/a[8]')
ActionChains(driver).move_to_element[element].perform()
# 单击，弹出的Ajax元素，根据链接节点的内容查找driver.find_element_by_link_text('高级搜索').click()
```
## selenium - 切换页面
* 适用网站
```
页面中点开链接出现新的页面,但是浏览器队形browser还是之前的对象
```
* 应对方案
```
# 获取当前所有句柄(窗口)
all_handles = browser.window_handles
# 切换browser到新的窗口,获取新的对象
browser.switch_to.window(all_handles[1])
```
## 网站案例
* 目标
```
1. 将民政区划代码爬取到数据库中，按照层级关系(分表 -- 省表、市表、县表)
2. 增量抓取 - 如果网站未更新，则不抓
```
* 数据库中建表
```
# 建库
create database govdb charset utf8;
use govdb;
# 建表
create table province(
    p_name varchar(20),
    p_code varchar(20)
)charset=utf8;
create table city(
    c_name varchar(20),
    c_code varchar(20),
    c_father_code varchar(20)
)charset=utf8;
create table country(
    x_name varchar(20),
    x_code varchar(20),
    x_father_code varchar(20)
)charset=utf8;
```
* 思路
```
1. selenium + chrome打开一级页面,并提取最新区划代码链接
2. 增量爬取:和数据库version表进行比对，确定之前是否爬过(是否有更新)
3. 如果没有更新，直接提示用户，无序继续爬取
4. 如果有更新，则删除之前表中数据，重新爬取并插入数据表
5. 最终完成后:断开数据库连接，关闭浏览器
```
* 代码实现
```

```
**SQL命令练习**
```
# 查询所有省市县信息(多表查询实现)
select province.p_name,city.c_name,country.x_name from province,city,country where province.p_code=city.c_father_code and city.c_code=country.x_father_code
# 查询所有省市县信息(连接查询实现)
select province.p_name,city.c_name,country.x_name from province inner join city on province.p_code=city.c_father_code inner join country on city.c_code=country.x_father_code;
```
## selenium -Web客户端验证
**弹框中的用户名和密码如何输入**
```
不用输入，在URL地址中填入就可以
```
**示例:爬取某一天笔记**
```
from selenium import webdriver
url = 'http://tarenacode:code_2013@code.tarena.com.cn/AIDCode/aid1905/14_spider/spider_day06.zip'
browser = webdriver.Chrome()
browser.get(url)
```
## selenium - iframe子框架
* 特点
```
网页中嵌套来了网页，先切换到iframe子框架,然后再执行其他操作
```
* 方法
```
browser.switch_to.iframe(iframe_element)
```
* 示例 -- 登录qq邮箱
```
https://mail.qq.com/
# iframe: login_frame
# 用户名: u
# 密码: p
# 登录: login_button
```
## 百度翻译破译案例
### 目标
```
破解百度翻译接口，抓取翻译结果数据
```
### 实现步骤
* F12抓包,找到json的地址,观察查询参数
```
1. POST地址:
https://fanyi.baidu.com/v2transapi
2. Form表单数据(多次抓取在变的字段)
    from: en
    to: zh
    query: dream
    simple_means_flag: 3
    sign: 679690.965691
    token: 815b3f89458ebbbecbd9a7d41b42cf4e # 基本固定，但也想办法获取
```
* 抓取相关JS文件
```
右上角 - 搜索 - sign: - 找到具体JS文件(index_c8a141d.js) - 格式化输出
```
* 在JS中寻找sign的生成码
```
1. 在格式化输出的JS代码中搜索:sign:找到如下JS代码:sign:m(a)
2. t通过设置断点,找到m(a)的函数的位置,即生成sign的具体函数
```
* 具体代码实现
```
1. 获取token和gtk的值
    GET:地址:百度翻译首页发送请求，从响应内容中获取
    https://fanyi.baidu.com/?aldtype=16047
2. POST请求
    https://fanyi.baidu.com/v2transapi
    requests.post(URL,data,headers=headers)
    
# formdata
data = {
    "from": "en",
    "to": "zh",
    "query": "hello",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "54706.276099",
    "token": "815b3f89458ebbbecbd9a7d41b42cf4e",
}  

# headers
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-length": "121",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "BIDUPSID=10654A2CFBEA2F15A893A2E2FF68A8A9; PSTM=1576175989; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BAIDUID=10654A2CFBEA2F150E0109A25E628154:SL=0:NR=10:FG=1; delPer=0; PSINO=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; sideAdClose=18249; H_PS_PSSID=1454_21116_30211_30283; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1576642503,1576764598,1576765700,1576767418; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1576767418; __yjsv5_shitong=1.0_7_95958817e0e9f0f806df35f4c7b00392d131_300_1576767421965_124.89.86.156_41c36524; yjs_js_security_passport=e67cadd372d2371c6436e1cc08c2961b9998eb55_1576767432_js",
    "origin": "https://fanyi.baidu.com",
    "pragma": "no-cache",
    "referer": "https://fanyi.baidu.com/?aldtype=16047",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

# 正则获取gtk + token
"window.gtk = '(.*?)'"
"token: '(.*?)'"
```
## Scrapy框架
* 定义
```
异步处理框架，可配置和可扩展程度非常高，Python中使用最广泛的爬虫框架
```
* 安装
```
# Ubuntu安装
1. 安装依赖包
    1. sudo apt-get install libffi-dev
    2. sudo apt-get install libssl-dev
    3. sudo apt-get install libxml2-dev
    4. sudo apt-get install python3-dev
    5. sudo apt-get install libxslt1-dev
    6. sudo apt-get install zlib1g-dev
    7. sudo apt-get install -I -U 
service_identity
2. 安装scrapy框架
    1. sudo pip3 install Scrapy
```
```
# Window安装
cmd命令行(管理员):python -m pip install Scrapy
# Error:Microsoft Visual C++ 14.0 is required xxx
```
* Scrapy框架五大组件
```
1. 引擎(Engine)       : 整个框架的核心
2. 调度器(Scheduler)  : 维护请求队列
3. 下载器(Downloader) : 获取响应对象
4. 爬虫文件(Spider)   : 数据解析提取
5. 项目管道(pipeline) : 数据入库处理
****************************************
# 下载器中间件(Downloader Middlewares):引擎->下载器,包装请求(随机代理)
# 蜘蛛中间件(Spider Middlewares):引擎->爬虫文件，可修改响应对象属性
```
- **scrapy爬虫工作流程**

```
# 爬虫项目启动
1、由引擎向爬虫程序索要第一个要爬取的URL,交给调度器去入队列
2、调度器处理请求后出队列,通过下载器中间件交给下载器去下载
3、下载器得到响应对象后,通过蜘蛛中间件交给爬虫程序
4、爬虫程序进行数据提取：
   1、数据交给管道文件去入库处理
   2、对于需要继续跟进的URL,再次交给调度器入队列，依次循环
```

**常用命令**

```

```

### **今日作业**

```
1、熟练使用 execjs 模块
2、熟记scrapy框架的组件及工作流程 - 要求能口头描述清楚
```




