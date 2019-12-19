# Day10
## Day09回顾
### 多线程爬虫
* 思路
```
1. 将待爬取的URL地址存放到队列中
2. 多个线程从队列中获取地址,进行数据抓取
3. 注意获取地址过程中程序阻塞问题
    # 写法一
    while True:
        if not q.empty()
            url = q.get()
            ... ... 
        else:
            break
    # 写法二
    while True:
        try:
            url = q.get(block=True,timeout=3)
        except Exception as e:
            break
```
* 将抓取数据保存到同一文件
```
# 注意多线程写入的线程锁问题
from threading import Lock
lock = Lock()
lock.acquire()
python代码块
lock.release()
```
* 实现思路
```
# 1. 在__init__(self)中创建文件对象，多线程操作此对象进行文件写入
    self.f = open('xiaomi.csv','a',newline='')
    self.writer = csv.writer(self.f)
    self.lock = Lock()
# 2. 每个线程抓取1页数据后将数据进行写入，写入文件时需要加锁
    def parse_html(self):
        app_list = []
        for xxx in xxx:
            app_list.append([name,link,typ])
        self.lock.acquire()
        self.writer.writerows(app_list)
        self.lock.release()
# 3. 所有数据抓取完成关闭文件
    def main(self):
        self.close()
```
## 解析模块汇总
re、lxml+xpath、json
```
# re
import re
pattern = re.compile(r'',re.S)
r_list = pattern.findall(html)

# lxml+xpath
from lxml import etree
parse_html = etree.HTML(html)
r_list = parse_html.xpath('')

# json
# 响应内容由json转为python
html = json.loads(res.text)
# 所抓取数据保存到json文件
with open('xxx.json','a') as f:
    json.dump(item_list,f,ensure_ascii=False)
# 或
f =open('xxx.json','a')
json.dump(item_list,f,ensure_ascii=False)
f.close()
```
# Day07笔记
## cookie模拟登陆
### 适用场景
```
抓取需要登录才能访问的页面
```
### cookie和session机制
```
# http协议为无连接协议
cookie:存放在客户端浏览器
session:存放在web服务器
```
##人人网登录案例
* 方法一 - 登录网站手动抓取Cookie
```
1. 先登录成功1次，获取到携带登录信息的cookie
    登陆成功 - 个人主页 - F12抓包 - 刷新个人主页 - 找到主页的包(profile)
2. 携带者Cookie发请求
    ** Cookie
    ** User-Agent 
```
```
import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # 抓取的url地址
        self.url = 'http://www.renren.com/973116780/profile'
        self.headers = {
            'Cookie': 'anonymid=k4c0r1yz-pzvxkf; depovince=GW; _r01_=1; JSESSIONID=abcDAiw02y0mU64ddRB8w; ick_login=83f80a9a-2b55-40f3-8685-88a6144f0626; t=f41b47d87ea76c271cb60f84bd6706660; societyguester=f41b47d87ea76c271cb60f84bd6706660; id=973116780; xnsid=e4530f4b; ver=7.0; loginfrom=null; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341787; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341792; wp_fold=0; jebecookies=cd8b6928-eee7-4bde-a161-7933a4f284d8|||||; XNESSESSIONID=ead277ab8d81',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }

    def get_parse_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        # r_list['就读于国家检察官学院']
        print(r_list)

    def run(self):
        self.get_parse_html()


if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()
```
* 方法二 - requests模块处理Cookie
**原理思路及实现**
```
# 1. 思路
requests模块提供了session类，来实现客户端和服务端的会话保持
# 2. 原理
1. 实例化session对象
    session = requests.session()
2. 让session对象发送get或者post请求
    res = session.post(url=url,data=data,headers=headers)
    res = session.get(url=url,headers=headers)
# 3. 思路梳理
浏览器原理:访问需要登录的页面会带着之前登录过的cookie
程序原理:同样带着之前登录的cookie去访问 - 由session对象完成
1. 实例化session对象
2. 登录网站:session对象发送请求，登录对应网站，把cookie保存在session对象中
3. 访问页面:session能够自动携带之前的这个cookie进行请求
```
**具体步骤**
```
1. 寻找Form表单提交地址 - 登录时的POST的地址
    查看网页源码,查看form表单，找action对应的地址
    http://www.renren.com/PLogin.do
2. 发送用户名和密码信息到POST的地址
    * 用户名和密码信息以什么方式发送？ --  字典
        键:<input>标签中的name的值(email,password)
        值:真实的用户名和，密码
        post_data = {'email':'','password':''}
session = requests.session() 
session.post(url=url,data=data)
```
**程序实现**
```
import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # post_url为form表单中action对应的URL地址
        self.post_url = 'http://www.renren.com/PLogin.do'
        # 真正要抓取的页面的url地址 - 个人主页
        self.get_url = 'http://www.renren.com/970294164/profile'
        # 实例化session = requests.session()
        self.session = requests.session()
    # 提取数据 - 先post再get
    def parse_html(self):
        data = {
            'email':'15110225726',
            'password':'zhanshen001'
        }
        # 1. 先post,把cookie保存在session对象中 - 会话保持
        self.session.post(url=self.post_url,data=data)
        # 再get,正常抓取数据
        html = self.session.get(url=self.get_url).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        print(r_list)

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()

```
* 方法三
**原理**
```
1. 把抓取到的cookie处理为字典
2. 使用requests.get()中的参数:Cookies
res = requests.get(
    url=url,
    params=params,
    auth=auth,
    proxies=proxies,
    headers=headers,
    timeout=5,
    cookies=cookies, # cookies也为字典
)
```
**处理cookie为字典**
```
    def get_cookies(self):
        cookies = {}
        cookies_str = 'anonymid=k4c0r1yz-pzvxkf; depovince=GW; _r01_=1; JSESSIONID=abcDAiw02y0mU64ddRB8w; ick_login=83f80a9a-2b55-40f3-8685-88a6144f0626; t=f41b47d87ea76c271cb60f84bd6706660; societyguester=f41b47d87ea76c271cb60f84bd6706660; id=973116780; xnsid=e4530f4b; ver=7.0; loginfrom=null; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341787; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341792; wp_fold=0; jebecookies=cd8b6928-eee7-4bde-a161-7933a4f284d8|||||; XNESSESSIONID=ead277ab8d81'
        for kv in cookies_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value
        return cookies
```
**代码实现**
```
import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # 抓取的url地址
        self.url = 'http://www.renren.com/973116780/profile'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }

    def get_cookies(self):
        cookies = {}
        cookies_str = 'anonymid=k4c0r1yz-pzvxkf; depovince=GW; _r01_=1; JSESSIONID=abcDAiw02y0mU64ddRB8w; ick_login=83f80a9a-2b55-40f3-8685-88a6144f0626; t=f41b47d87ea76c271cb60f84bd6706660; societyguester=f41b47d87ea76c271cb60f84bd6706660; id=973116780; xnsid=e4530f4b; ver=7.0; loginfrom=null; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341787; jebe_key=77eabbe7-277c-4414-ab89-64253f69f03f%7Cccea8a8b81a47ac4b3a5c48154653dfb%7C1576717335984%7C1%7C1576717341792; wp_fold=0; jebecookies=cd8b6928-eee7-4bde-a161-7933a4f284d8|||||; XNESSESSIONID=ead277ab8d81'
        for kv in cookies_str.split('; '):
            key = kv.split('=')[0]
            value = kv.split('=')[1]
            cookies[key] = value
        return cookies

    def get_parse_html(self):
        cookies = self.get_cookies()
        html = requests.get(
            url=self.url,
            headers=self.headers,
            # cookies参数,类型为字典
            cookies=cookies,
        ).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        # r_list['就读于国家检察官学院']
        print(r_list)

    def run(self):
        self.get_parse_html()


if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()
```
## json解析模块
**json.loads(json)**
* 作用
```
把json的字符串转为python数据类型
```
* 示例
```
html_json = json_loads(res.text)
```
**json.dumps(python)**
* 作用
```
把python类型转为json类型
```
* 示例
```
import json

# json.dumps()之前
item = {'name':'QQ','app_id:1'}
print('before dumps',type(item)) # dict
# json.dumps之后
item = json.dumps(item)
print('after dumps',type(item)) # str
```
**json.load(f)**
* 作用
```
将json文件读取,并转为python类型
```
* 示例
```
import json
with open('day10/xiaomi.json','r') as f:
    data = json.load(f)
print(data)
```
**json.dump(python,f,ensure_ascii=False)**
* 作用
```
把python数据类型转为json的字符串
# 一般让你把抓取的数据保存到json文件时使用
```
* 参数说明
```
第1个参数:python数据类型的数据(字典，列表等)
第2个参数:文件对象
第3个参数:ensure_ascii=False # 序列化时编码
```
* 示例1
```
import json
item = {'name':'QQ','app_id':1}
with open('小米.json','a',encoding='utf-8') as f:
    json.dump(item,f,ensure_ascii=False)
```
* 示例2 
```
import json
item_list = []
for i in range(3):
    item = {'name':'QQ','id':i}
    item_list.append(item)
with open('xiaomi.json','a') as f:
    json.dump(item_list,f,ensure_ascii=False)
```
### json模块总结
```
# 爬虫最常用
1. 数据抓取 - json.loads(html)
    将响应内容由:json转为python
2. 数据保存 
    json.dump(item_list,f,ensure_ascii=False)
    将抓取的数据保存到本地json文件
# 抓取数据一般处理方式
1. txt文件
2. csv文件
    import csv
    with open('xxx.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerows([(),()])
3. json文件
    import json
    with open('xxx.json','a') as f:
        json.dump(app_list,f,ensure_ascii=False)
4. MySQL数据库
    import pymysql
    db = pymysql.connect(xx,xx,xx)
    cursor = db.cursor()
    抓数据
    cursor.execute('',[])
    db.commit()
    db.close()
5. MongoDB数据库
    import pymongo
    conn = pymongo.,MongoClient('',27017)
    db = conn['库名']
    myset = db['集合名']
    抓数据
    myset.insert_one({})
6. Redis数据库
```
## selenium+phantomjs/Chrome/Firefox
**selenium**
* 定义
```
1. web自动化测试工具,可运行在浏览器,根据指令操作浏览器
2. 只是工具,必须与第三方浏览器结合使用
```
* 安装
```
Linux:sudo pip3 install selenium
Windows: python -m pip install selenium
```
**phantomjs浏览器**
```
无界面浏览器(又称无头浏览器),在内存中进行页面加载,高效
```
**phantomjs、chromedriver,geckodriver**
* Windows
```
1. 下载对应版本的phantomjs,chromedriver,geckodriver
2. 把chromedriver.exe拷贝到python安装目录的scripts目录下(添加到系统环境变量)
    # 查看python安装路径:where python
3. 验证
    cmd命令行:chromedriver
# 下载地址
1. chromedriver: 下载对应版本
    http://chromedriver.storage.googleapis.com/index.html
2. geckodriver
    https://github.com/mozilla/geckodriver/releases
3. phantomjs
    https://phantomjs.org/download.html
```
* Linux
```
1. 下载解压
    tar -zxvf geccodriver.tar.gz
2. 拷贝解压后文件到 /usr/bin/ (添加环境变量)
    sudo cp geckodriver /usr/bin/
3. 更改权限
    sudo -i
    cd /usr/bin
    chromed 777 geckodriver
```
* 使用
示例代码一:使用selenium+浏览器+百度
```
# 导入selenium的webserver接口
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r"D:\Chrome\Application\chrome.exe"
# 1. 创建浏览器对象 - 打开浏览器
browser = webdriver.Chrome(chrome_options=options)
# browser = webdriver.PhantomJS()
# 2. 地址栏输入百度地址
browser.get('http://www.baidu.com/')
# 获取快照
# browser.save_screenshot('baidu.jpg')
# 3. 停留5秒
time.sleep(5)
# 4. 关闭浏览器
browser.quit()
```
* 浏览器对象(browser)方法
```
# from selenium import webdriver
1. browser = webdriver.Chrome(executable_path='path')
# get()等页面所有元素加载完成后才会执行代码
2. browser.get(url)
3. browser.page_source # HTML结构源码
4. browser.page_source.find('字符串')
    # 从html源码中搜索指定字符串，没有找到返回:-1
5. browser.quit() # 关闭浏览器 
```
* 定位节点
**单元素查找(1个节点对象)**
```
1. browser.fin_element_by_id('')
2. browser.fin_element_by_name('')
3. browser.fin_element_by_class_name('')
4. browser.fin_element_by_xpath('')
... ...
```
**多元素查找[节点对象列表]**
```
1. browser.fin_elements_by_id('')
2. browser.fin_elements_by_name('')
3. browser.fin_elements_by_class_name('')
4. browser.fin_elements_by_xpath('')
# 示例
li_list = browser.find_elements_by_xpath('')
for li in li_list:
    name = li.find_element_by_xpath('./')
    star = li.find_element_by_xpath('.//')
```
* 节点对象操作
```
1. ele.send_keys('') # 搜索发送内容
2. ele.click()
3. ele.text # 获取文本内容,包含子节点和后代节点的文本
4. ele.get_attribute('src') # 获取属性值
```
## 京东爬虫案例
* 目标
```
1. 目标地址:https://www.jd.com/
2. 抓取目标:商家名称、商品价格、评价数量、商品商家
```
* 思路提醒
```
1. 打开京东，到商品搜索页
2. 匹配所有商品节点对象列表
3. 把节点对象的文本内容取出来，查看规律，是否有更好的处理方法
4. 提取完1页后，判断如果不是最后1页，则点击下一页
   # 如何判断是否为最后一页？？
```
* 实现步骤
**找节点**
```
1. 首页搜索: //*[@id="key"]
2. 首页搜索按钮: //*[@id="search"]/div/div[2]/button
3. 商品页的商品信息节点对象列表: //*[@id="J_goodsList"]/ul/li
4. for循环遍历后
    名称: .//div[@class="p-name"]/a/em
    价格: .//div[@class="p-price"]
    评论: .//div[@class="p-commit"]/strong
    商家: .//div[@class="p-shopnum"]
```
执行JS脚本，获取动态加载数据

```
browser.execute_script(
  'window.scrollTo(0,document.body.scrollHeight)'
)
```

代码实现

```

```

**selenium-切换页面(句柄)**

- **适用网站**

```

```

- **应对方案**

```
# 1.获取当前所有句柄(窗口):列表 [<page1>,<page2>]
all_handles = browser.window_handles
# 2.切换句柄
browser.switch_to.window(all_handles[1])
```

**今日作业**

```
民政部数据抓取: selenium + Chrome
1、增量爬取
2、分表存储数据
   省表:province : name code
   市表:city     : name code 对应省的编号
   县表:county   : name code 对应市的编号
把数据判断后存入到对应表中
```






