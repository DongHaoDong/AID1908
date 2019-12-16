# Day04回顾
## 请求模块(urllib.request)
```
req = request.Request(url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
```
## 编码模块(urllib.parse)
```
1. urlencode({dict})
    urlencode({'wd':'美女','pn':'20'})
    编码后:'wd=%E7%BE%8E%E5%A5%B3&pn=20'
2. quote(string)
    quote('织女')
    编码后 : '%D3%F5XXX'
3. unquote('%D3%F5XXX')
```
## 解析模块(re)
* 使用流程
```
pattern = re.compile('正则表达式',re.S)
r_list = pattern.findall(html)
```
* 贪婪匹配和非贪婪匹配
```
贪婪匹配(默认) : .*
非贪婪匹配 : .*?
```
* 正则表达式分组
```
1. 想要什么内容在正则表达式中加()
2. 多个分组,先按整体正则匹配，然后再提取()中数据。结果:[(),(),(),(),()]
```
## 抓取步骤
```
1. 确定所抓取数据在响应中是否存在(右键-查看网页源码-搜索关键字)
2. 数据存在:查看URL地址规律
3. 写正则表达式，来匹配数据
4. 程序结构
    1. 使用随机User-Agent
    2. 每爬取一个页面后随机休眠一段时间
```
```
# 程序结构
class xxxSpider(object):
    def __init__(self):
    # 定义常用变量,url,headers及计数等
    
    def get_html(self):
    # 获取响应内容函数，使用随机User-Agent
    
    def parse_html(self):
    # 使用正则表达式来解析页面，提取数据
    
    def write_html(self):
    # 将提取的数据按要求保存，csv,MySQL数据库等
    
    def main(self):
        # 主函数用来控制整体逻辑
        
if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = xxxSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f'%(end-start))
```
# Day02笔记
## 作业讲解
### 作业1-正则分组练习
页面结构如下:
```html
<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small while rabbit white and white
    </p>
</div>
```
从以上html代码结构中完成如下内容信息的提取
```
# 问题1
[('Tiger','Two...'),('Rabbit','Small...')]
# 问题2
动物名称:Tiger
动物描述:Two tigers two tigers run fast
**********************************************
动物名称:Rabbit
动物描述:Small while rabbit while and white
```
* 代码实现
```
import re
html='''
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small while rabbit white and white
    </p>
</div>
'''
# r_list:[('Tiger','\n Two ...')]
# 问题1
re_bds = '<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>'
pattern = re.compile(re_bds,re.S)
r_list = pattern.findall(html)
# 问题2
for r in r_list:
    print('动物名称:',r[0].strip())
    print('动物描述:',r[1].strip())
    print('*' * 50)
```
### 猫眼电影top100抓取案例
```
猫眼电影 - 榜单 - top100榜
电影名称 - 主演 - 上映时间
```
#### 数据抓取实现
* 1. 确定响应内容中是否存在所需数据
```
右键 - 查看网页源代码 - 搜索关键字 - 存在！！
```
* 2. 找URL规律
```
第1页:https://maoyan.com/board/4?offset=0
第2页:https://maoyan.com/board/4?offset=10
第n页:offset=(n-1)*10
```
* 3. 正则表达式
```
<div class="movie-item-info">.*?title="(.*?)"class="star">(.*?)</p>.*?releasetime">(.*?)</p>
``` 
* 4. 编写程序框架，完善程序
```
from urllib import request
import re
import time
import random
from useragents import ua_list

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 添加计数变量
        self.i = 0
    # 请求
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析
    def parse_html(self,html):
        # r_list:[('月光宝盒'),('周星驰'),(1994-01-01)]
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(r_list)

    # 保存
    def write_html(self,r_list):
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            print(item)
            self.i += 1
    # 主函数
    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 随机休眠 - uniform生成随机的浮点数
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%2.f'%(end-start))
```
# 数据持久化存储
## 数据持久化存储 - csv文件
* 作用
```
将爬取的数据存放到本地的csv文件中
```
* 使用流程
```
1. 导入模块
2. 打开csv文件
3. 初始化写入对象
4. 写入数据(参数为列表)
import csv
with open('film.csv','w') as f:
    writer = csv.write(f)
    writer.writerow([])
```
* 示例代码
创建test.csv文件，在文件中写入数据
```
# 单行写入(writerow([]))
import csv 
with open('test.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['步惊云','36'])
    writer.writerow(['聂风','25'])
# 多行写入(writerows([(),(),()]))
# newline='':在windows中默认会添加一个空行
import csv
with open('test.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows([('聂风','36'),('秦霜','25'),('孔慈','30')])
```
* 练习
猫眼电影数据存入本地maoyanfilm.csv文件-使用writerow()方法实现
```
from urllib import request
import re
import time
import random
from useragents import ua_list
import csv

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 添加计数变量
        self.i = 0
    # 请求
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析
    def parse_html(self,html):
        # r_list:[('月光宝盒'),('周星驰'),(1994-01-01)]
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(r_list)

    # 保存 - writerow()
    # def write_html(self,r_list):
    #     item = {}
    #     # 以a的方式打开文件，如果以w方式打开文件则只保留最后一页数据
    #     with open('maoyan.csv','a',newline='') as f:
    #         writer = csv.writer(f)
    #         for r in r_list:
    #             item['name'] = r[0].strip()
    #             item['star'] = r[1].strip()
    #             item['time'] = r[2].strip()[5:15]
    #             print(item)
    #             L = [item['name'],item['star'],item['time']]
    #             writer.writerow(L)
    #             self.i += 1
    def write_html(self,r_list):
        L = []
        item = {}
        # 以a的方式打开文件，如果以w方式打开文件则只保留最后一页数据
        with open('maoyan.csv','a',newline='') as f:
            writer = csv.writer(f)
            for r in r_list:
                item['name'] = r[0].strip()
                item['star'] = r[1].strip()
                item['time'] = r[2].strip()[5:15]
                print(item)
                t = (item['name'],item['star'],item['time'])
                L.append(t)
                self.i += 1
            writer.writerow(L)
    # 主函数
    def run(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 随机休眠 - uniform生成随机的浮点数
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%2.f'%(end-start))
```
## 数据持久化存储-MySQL数据库
### 在数据库中建库建表
```
# 连接mysql数据库
mysql -u root -p584023982
# 建库建表
create database maoyandb charset utf8;
use maoyandb;
create table filmtab(
    name varchar(100),
    star varchar(300),
    time varchar(50)
)charset=utf8;
```
### 回顾pymysql基本使用
```
import pymysql
# 创建2个对象
db = pymysql.connect('127.0.0.1','root','584023982','maoyandb',charset='utf8')
cursor = db.cursor()
# 执行SQL命令并提交到数据库执行
# execute()方法第二个参数为列表传参补位
ins = 'insert into filmtab values(%s,%s,%s)'
cursor.execute(ins,['霸王别姬','张国荣','1993'])
db.commit()
# 关闭
cursor.close()
db.close()
```
* 来试试高效的executemany()方法
```
import pymysql

# 创建2个对象
db = pymysql.connect('127.0.0.1','root','584023982','maoyandb',charset='utf8')
cursor = db.sursor()
# 抓取的数据
film_list = [('月光宝盒','周星驰','1994'),('大圣娶亲','周星驰','1994')]
# 执行SQL命令并提交到数据库执行
# execute()第二个参数为列表传参补位
cursor.executemany('insert into filmtab values(%s,%s,%s)',film_list)
db.commit()
# 关闭
cursor.close()
db.close()
```
* 4. 做个SQL查询
```
1. 查询20年以前的电影的名字和上映时间
SELECT NAME,TIME FROM filmtab WHERE TIME<(NOW()-INTERVAL 20 YEAR);
2. 查询1990-2000年的电影名字和上映时间
SELECT NAME,TIME FROM filmtab WHERE TIME>='1990-01-01' AND TIME<='2000-12-31';
```
## 数据持久化存储-MongoDB数据库
```
MongoDB是一个基于磁盘的菲关系型(key-value)数据库，value为json串
MySQL:库 表 表记录
Mongo:库 集合 文档
```
### pymongo操作mongodb数据库
```
import pymongo

# 创建数据库连接对象
conn = pymongo.MongoClient('127.0.0.1',27017)
# 库对象
db = conn['库名']
# 3.集合对象
myset = db['集合名']
# 4. 插入数据
myset.insert_one({字典})
```
### mongodb常用命令
```
1. mongo                    # 进入到mongo数据库
2. show dbs                 # 查看所有库
3. use 库名                  # 切换库
4. show collections         #查看当前库中所有集合
5. db.集合名.find().pretty() # 格式化输出文档
6. db.集合名.count()         # 统计集合中文档个数
7. db.dropDatabase()        # 删除库
```
### 思考
```
1. 能否到电影详情页把评论抓取下来?
2. 能否到电影详情页把电影图片抓取下来? - 并按照电影名称分别创建文件夹
```
### 代码实现
```
from urllib import request
import re
import time
import random
from useragents import ua_list
import csv
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 添加计数变量
        self.i = 0

    # 请求
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)
        # 创建3个对象
        self.conn = pymongo.MongoClient('127.0.0.1',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['filmtab']


    # 解析
    def parse_html(self,html):
        # r_list:[('月光宝盒'),('周星驰'),(1994-01-01)]
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(r_list)
    # 保存
    def write_html(self,r_list):
        for r in r_list:
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()[5:15]
            # 插入到monggodb数据库中
            self.myset.insert_one(item)
    # 主函数
    def run(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 随机休眠 - uniform生成随机的浮点数
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%2.f'%(end-start))
```

