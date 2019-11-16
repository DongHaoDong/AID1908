# MySQL基础回顾
WEB前端+后端+爬虫+数据分析+人工智能
## 1. 数据库概念
1. 数据库
    * 存储数据的仓库(逻辑概念，并未真实存在)  
3. 数据库软件
    * 真实软件，用来实现数据库这个逻辑概念
2. 数据仓库
    * 数据量更加庞大，更加侧重数据分析和数据挖掘，供企业决策分析之用，主要是数据查询，修改删除很少
## 2. MySQL特点
* 关系型数据库
* 跨平台
* 支持多种编程语言(python、Java、php)
* 基于磁盘存储，数据是以文件形式存放在数据库目录/var/lib/mysql下
## 3. 启动连接
* 服务启动
```
sudo /etc/init.d/mysql start|stop|restart|status
sudo service mysql start|stop|restart|status
```
* 客户端连接
```
mysql -hIp地址 -u用户名 -p密码
本地可省略 -h 选项
```
## 4. 基本SQL命令
库管理
```
1. 查看数据库
show databases;
2. 创建数据库并指定字符集
create database 数据名 charset utf8; 
3. 查看当前所在库
select database();
4. 切换库
use 数据库名;
5. 查看库中已有表
show tables;
6. 删除库
drop database 数据库名;
```
表管理
```
1. 创建表并指定字符集
create table 表名(字段名 字段类型  xxx,)charset=utf8
2. 查看创建表语句(字符集、存储引擎)
show create table 表名;
3. 查看表结构
desc 表名
4. 删除表
drop 表名
```
表记录管理
```
1. 增
insert into 表名(字段名) values(),();
2. 删
delete from 表名 where 条件;
3. 改
update 表名 set 字段名=值,字段名=值 where 条件;
4. 查
select 字段名/* from 表名 where 条件;
```
表字段管理(alert table 表名)
```
1. 增
alert table 表名 add 字段名 字段类型 first | after 字段名
2. 删
alert table 表名 drop 字段名;
3. 改
alter table 表名 modify 字段名 新类型; 
4. 表重命名 
alter table 表名 rename 新表名;
```
## 5. 数据类型
四大数据类型
* 数值类型
```
int smallint bigint tiny
float(m,n) double decimal 
```
* 字符类型
```
char() varchar() text blob
```
* 枚举类型
```
enum()    set()
```
* 日期时间类型
```
date time year datetime timestamp
```
日期时间函数
```
NOW() CURDATE() YEAR(字段名) DATE(字段名) TIME(字段名)
```
日期时间运算
```
select * from 表名 where 字段名 运算符(NOW()-interval 间隔);
间隔单位：1 day | 3 month | 2 year
eg1:查询1年以前的用户充值信息
select * from user where time <(NOW()-interval 1 year);
```
## 6. MySQL运算符
* 数值比较
```
> >= < <= = !=
eg1:查询成绩不及格的学生
select * from students where socre < 60;
eg2:删除成绩不及格的学生
delete from students where score < 60;
eg3:把id为3的学生的姓名改为周芷若
update students set name = "周芷若" where id = 3;
```
* 逻辑比较
```
and or
eg1:查询成绩不及格的男生
select * from students where gender = "M" and score < 60;
eg2:查询成绩在60-70之间的学生
select * from students where score >= 60 and score < 70;
```
* 范围内比较
```
between 值1 and 值2、 in() not in()
eg1:查询不及格的学生姓名及成绩
select name,score from students where score between 0 and 59;
eg2:查询AID1905和AID1903班学生姓名及成绩
select name,score from where class in ('AID1905','AID1903');
```
* 模糊比较(like)
```
where 字段名 like 表达式(%_)
eg1:查询北京的姓赵的学生信息
select * from students where address = "北京" and name like "赵%";
```
* null判断
```
is NULL、is not NULL
eg1:查询姓名字段值为NULL的学生信息
select * from students where name is NULL;
```
## 7. 查询
* order by
给查询的结果进行排序(永远放在SQL命令的倒数第二的位置写)
```
order by 字段名 ASC/DESC
eg:查询成绩从高到低排列
select * from students order by score DESC; 
```
* limit
限制显示查询记录的条数(永远放在SQL命令的最后写)
```
limit n:显示前n条  
limit m,n:从第(m+1)条记录开始，显示n条  
分页:每页显示10条，显示第6页的内容  
limit(6-1)*10 10  
(m-1)*n,n    m为要显示的页数,n为每页显示数据条数
```
# MySQL高级-Day01
## MySQL基础巩固
* 创建库：country(指定字符编码为utf8)
* 创建表：sanguo 字段:id,name,attack,defense,gender('M'|'F'),country  
要求：id为主键，并设置自增长属性
id int primary key auto_increment,
* 插入5条表记录(id 1-5,name-诸葛亮、司马懿、貂蝉、张飞、赵云),攻击>100 ,防御<100)
* 查找所有蜀国人的信息
```
SELECT * FROM sanguo WHERE country ="蜀国";
```
* 将赵云的攻击力设置为360,防御力设置为68;
```
UPDATE sanguo SET attack=360,defense=68 WHERE NAME="赵云";
```
* 将吴国英雄中攻击值为120的英雄攻击值改为100，防御力改为60
```
UPDATE sanguo SET attack=100,defense=60 WHERE attack=120 AND country="吴国";
```
* 找出攻击值高于200的蜀国英雄的名字、攻击力
```
SELECT NAME,attack FROM sanguo WHERE country = "蜀国" AND attack > 200; 
```
* 将蜀国英雄按攻击力从高到低排序
```
SELECT * FROM sanguo WHERE country = "蜀国" ORDER BY attack DESC;
```
* 魏蜀来光顾哦英雄中名字为三个字的按防御值从高到低排序
```
SELECT * FROM sanguo WHERE country IN ('魏国','蜀国') AND NAME LIKE '___' ORDER BY defense ASC;
```
* 在蜀国英雄中，查找攻击力前三名且名字不为null的英雄的姓名、攻击值、国家
```
SELECT NAME,attack,country FROM sanguo WHERE  NAME IS NOT NULL AND country = "蜀国" ORDER BY attack DESC LIMIT 3;
```
## MySQL普通查询
```
1. select ...聚合函数 from 表名
2. where ...
3. group by ...
4. having ...
5. order by ...
6. limit ...;
```
* 聚合函数
|方法|功能|
|----|----|
|avg(字段名)|该字段的平均值|
|max(字段名)|该字段的最大值|
|min(字段名)|该字段的最小值|
|sum(字段名)|该字段所有记录的和|
|count(字段名)|统计该字段记录的个数|
eg1:找出表中的最大攻击力的值
```
select max(attack) from sanguo;
```
eg2:表中共有多少个英雄
```
select count(id) as number from sanguo;
```
eg:蜀国英雄中攻击力大于200的英雄数量
```
select count(id) as number from sanguo where country="蜀国" and attack > 200;
```
* group by
给查询结果进行分组  
eg1:计算每个国家的平均攻击力
```
SELECT country,AVG(attack) FROM sanguo GROUP BY country;
```
eg2:所有国家的男英雄中英雄数量最多的前两名的国家名称及英雄数量
```
SELECT country,COUNT(id) AS number FROM sanguo WHERE gender="M" GROUP BY country ORDER BY  number DESC LIMIT 2; 
```
==group by后字段名必须要为select后的字段==  
==查询字段和group by后字段不一致，则必须对该字段进行聚合处理(聚合函数)==
* having语句
对分组聚合后的结果进行进一步筛选  
eg1:找出平均攻击力大于105的国家的前两名，显示国家名称和平均攻击力
```
SELECT country,AVG(attack) AS number FROM sanguo GROUP BY country HAVING number>105 ORDER BY number DESC LIMIT 2;
```
注意
```
having语句通常与group by联合使用
having语句存在弥补了where关键字不能与聚合函数联合使用的不足，where只能操作表中实际存在的字段，having操作的是聚合函数生成的显示列
```
* distinct语句
不显示字段的重复值
```
eg1:表中都有哪些国家
SELECT DISTINCT country FROM sanguo;
eg2:计算一共有多少个国家
SELECT COUNT(DISTINCT country) AS number FROM sanguo;
```
注意
```
distinct和from之间所有字段都相同才会去重
distinct不能对任何字段做聚合处理
```
* 查询表记录时做数学运算
运算符：+ - * / % **
```
eg1:查询时显示攻击力翻倍
SELECT NAME,attack*2 FROM sanguo;
eg2:更新蜀国所有英雄攻击力*2
UPDATE sanguo SET attack=attack*2 WHERE country="蜀国";
```
# 索引概述
* 定义
对数据表的一列或多列的值进行排序的一种结构(Btree方式)  
B树的特点->1.全部节点均包含索引+数据   
B树的特点->2. 范围查询->从根节点遍历至指定数据  
B+树的特点->1.非叶子节点值保存索引【树宽度优于B树，从而降低了磁盘IO】  
B+树的特点->2.叶子节点保存所有的索引和数据  
B+树的特点->3.叶子节点之间相互连接，形成链表结构  
【范围查询】

* 优点
加快数据检索速度
* 缺点
```
占用物理存储空间(/var/lib/mysql)
当对表中数据更新时，索引需要动态维护，降低数据维护速度
```
* 索引示例
```html
# cursor.executemany(SQL,[data1,data2,data3])
# 以此IO执行多条表记录操作，效率高，节省资源
1.开启运行时间检测
mysql>show variables like '%pro';
mysql>set profiling=1;
2.执行查询语句(无索引)
select name="Dream99999";
3. 查看执行时间
show profiles;
4. 在name字段创建索引
create index name on students(name);
5. 再次执行查询语句
select name="Dream99999";
6. 查看执行时间
show profiles;
```
# 索引的分类
## 普通(MUL) and 唯一(UNI)
* 使用规则
```
1. 可以设置而多个字段
2. 普通索引：字段值无约束，KEY标志位MUL
3. 唯一索引(unique):字段值不允许重复，但可为NULL，KEY标志为UNI
4. 哪些字段创建索引:经常用来查询的字段，where条件判断字段，order by排序字段
``` 
* 创建普通索引and唯一索引
创建表时
```html
create table 表名(
    字段名 数据类型,
    字段名 数据类型,
    index(字段名),
    index(字段名),
    unique(字段名)
);
```
已有表中创建
```html
create [unique] index 索引名 on 表名(字段名);
```
* 查看索引
```html
1. desc 表名; -->KEY标志为：MUL、UNI
2. show index from 表名;
```
* 删除索引
```html
drop index 索引名 on 表名
```
##主键(PRI)and自增长(auto_increment)
* 使用规则
```
1. 只能有一个主键字段
2. 所带约束：不允许重复，却不能为NULL
3. KEY标志(primary):PRI
4. 通常设置记录编号字段id,能唯一锁定一条记录
```
* 创建  
创建表添加主键
```sql
create table student(
    id int auto_increment,
    name varchar(20),
    primary key(id)
)charset=utf8,auto_increment=1;## 设置自增长起始值
```
已有表添加主键
```html
alter table 表名 add primary key(id);
```
已有表中操作自增长属性
```html
1. 已有表中添加自增长属性
alter table 表名 modify id int auto_increment;
2. 已有表重新指定起始值
alter table 表名 auto_increment=20000;
```
* 删除
```html
1. 删除自增长属性(modify)
alter table 表名 modify id int;
2. 删除主键索引
alter table 表名 drop primary key;
```
# 今日作业
* 1. 习重新做一遍
* 2. 面试题
有一张文章评论表comment如下

|comment_id|article_id|user_id|date|
|----------|----------|-------|----|
|1|10000|10000|2018-01-30 09:00:00|
|2|10001|10001|2018-01-30 09:00:00|
|3|10002|10000|2018-01-30 09:00:00|
|4|10003|10015|2018-01-30 09:00:00|
|5|10004|10006|2018-01-30 09:00:00|
|6|10005|10006|2018-01-30 09:00:00|
|7|10006|10000|2018-01-30 09:00:00|
以上是一个应用的comment表格的一部分，请使用SQL语句找出本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序  
备注：  
comment_id为评论的id
article_id为被评论文章的id
user_id指用户id  
* 操作题

     




