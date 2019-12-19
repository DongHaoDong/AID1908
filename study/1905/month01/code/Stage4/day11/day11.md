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




