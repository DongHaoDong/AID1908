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
```

