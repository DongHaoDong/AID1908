# MySQL-Day02必须掌握
## 外键
1. 原理
```html
让当前表字段的值在另一张表的范围内去选择
```
2. 使用规则
```html
1. 数据类型要一致
2. 主表被参考字段必须为KEY的一种：PRI
```
3. 级联操作
```html
1. cascade:删除、更新同步(被参考字段)
2. restrict(默认):不让主表删除、更新
3. set null:删除、更新，从表该字段值设置为NULL
```
## 嵌套查询(子查询)
1. 定义
```html
把内层的查询结果做为外层查询的条件
```
## 多表查询 
1. 笛卡尔积
```html
多表查询不加where，一张表的每条记录分别和另一张表的所有记录匹配一遍
```
## 连接查询
分类
```html
1. 内连接(表1 inner join 表2 on 条件)
2. 外连接(表2 left|join 表2 on 条件)
    1. 左连接：以坐标为主显示查询结果
    2. 右连接：以右表为主显示查询结果
```
语法
```html
select 表名.字段名 from 表1 inner join 表2 on 条件
select 表名.字段名 from 表1 left join 表2 on 条件
select 表名.字段名 from 表1 right join 表2 on 条件
```
## 锁
1. 目的:解决客户端并发访问的冲突问题
2. 锁分类
```html
1. 锁类型:读锁、写锁
2. 锁粒度:行级锁(InnoDB)、表级锁(MyISAM)
```
## 数据导入
方式一(使用source命令)
```html
mysql>source /home/tarena/xxx.sql
```
方法二(使用load命令)
```html
1. 将导入文件拷贝到数据库搜索路径中
show variables like'secure%';
2. 在数据库中创建对应表
3. 执行数据导入语句
```
## 索引
定义
```html
对数据库表中一列或多列的值进行排序的一种结构(BTree)
```
优点
```html
加快数据的检索速度
```
缺点
```html
1. 占用实际物理存储空间
2. 索引需要动态维护，消耗资源，降低数据的维护速度
```
分类及约束
```html
1. 普通索引(MUL):无约束
2. 唯一约束(UNI):字段值不允许重复，但可以为NULL
3. 主键(PRI):字段值不允许重复，不可为NULL
4. 外键:让当前表字段的值在另一张表的范围内选择
```
# MySQL-Day03笔记
## 存储引擎
1. 定义
```html
处理表的处理器
```
2. 基本操作
```html
1. 查看所有存储引擎
mysql>show engines;
2. 查看已有表的存储引擎
mysql>show create table 表名;
3. 创建表时指定
create table 表名 (...)engine=MyISAM,charset=utf8,auto_increment=1000;
4. 已有表指定
alter table 表名 engine=InnoDB;
```
3. 常用存储引擎及特点
* InnoDB
    ```html
    1. 支持行级锁
    2. 支持外键、事务、事务回滚
    3. 表字段和索引同存储在一个文件中
      1. 表名.frm:表结构
      2. 表名.ibd:表记录及索引文件
    ```
* MyISAM
    ```html
    1. 支持表级锁
    2. 表字段和索引分开存储
      1. 表名.frm:表结构
      2. 表名.MYI:索引文件(my index)
      3. 表名.MYD:表记录(my data)
    ```
* MEMORY
    ```html
    1. 表记录存储在内存中，效率高
    2. 服务或主机重启，表记录清除
    ```
* 如何选择存储引擎
```html
1. 执行查询操作多的表,具体问题具体分析->InnoDB
2. 执行写操作多的表用InnoDB
3. 临时表:MEMORY
```
## MySQL的用户账户管理
1. 开启MySQL远程连接
```html
更改配置文件,重启服务
1. sudo su
2. cd /etc/mysql/mysql.conf.d
3. cp mysqld.cnf mysqld.cnf.bak
4. vi mysqld.cnf # 找到44行左右加# 注释
   # bind-address=127.0.0.1
   [mysqld]
   character_set_server=utf8
5. 保存退出
6. service mysql restart
vi使用:按a-->编辑文件-->ESC-->shift+:-->wq
```
2. 添加授权用户
```html
1. 用root用户登录mysql
mysql -u root -p584023982
2. 授权
grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
3. 刷新权限
flush privileges;
```
3. 权限列表
```html
all privileges、select、insert ...
库.表 : *.*代表所有库的所有表
```
4. 示例
```html
1. 添加授权用户work，密码123,，对所有库的所有表有所有权限
mysql>grant all privileges on *.* to 'work'@'%' identified by '123'
with grant option;
mysql>flush privileges;
2. 添加用户duty,对db2库中所有表有所有权限
```
## 事务和事务回滚
1. 事务定义
```html
一件事从开始发生到结束的过程
```
2. 作用
```html
确保数据的一致性，准确性，有效性
```
3. 事务操作
```html
1. 开启事务
mysql>begin;   # 方法一
mysql>start transaction;    # 方法二
2. 开始执行事务中的一条或多条SQL指令
3. 提交事务
mysql>commit;   # 事物中SQL命令都执行成功，提交到数据库，结束！
mysql>rollback;     # 有SQL命令执行失败，回滚到初始状态，结束！ 
```
## 事务的四大特性(ACID)
1. 原子性(atomicity)
    ```html
    一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能执行其中的一部分操作
    ```
2. 一致性(consistency)
    ```html
    数据库总是从一个一致性的状态转换到另一个一致性的状态
    ```
3. 隔离性(isolation)
    ```html
    一个事务所做的修改在最终提交之前，对其他事务是不可见的
    ```
4. 持久性(durability)
    ```html
    一旦事务提交，则其所作的修改会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
    ```
注意
```html
1. 事务只针对于表记录操作(增删改)有效，对于库和表的操作无效
2. 事务一旦提交结束，对数据库中数据的更改是永久性的
```
##E-R模型(Entry-Relationship)
1. 定义
    ```html
    E-R模型即 实体-关系 数据模型，用于数据库设计
    用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系
    ```
2. 实体、属性、关系
    * 实体
    ```html
    1. 描述客观事物的概念
    2. 表示方法:矩形框
    3. 实例：一个人、一本书、一杯咖啡、一个学生
    ```
    * 属性
    ```html
    1. 实体具有的某种特性
    2. 表示方法：椭圆形
    3. 示例
       学生属性：学号、姓名、年龄、性别、专业
       感受属性：悲伤、喜悦、刺激、愤怒
    ```
    * 关系
    ```html
    1. 实体之间的联系
    2. 一对一关联(1:1):老公对老婆
       A中的一个实体，B中只能有一个实体与其发生关联
       B中的一个实体，A中只能有一个实体与其发生关联
    3. 一对多关联(1:n):父亲对孩子
       A中的一个实体，B中有多个实体与其发生关联
       B中的一个实体，A中只能有一个实体与其发生关联
    4. 多对多关联(m:n):兄弟姐妹对兄弟姐妹、学生对课程
       A中的一个实体，B中有多个实体与其发生关联
       B中的一个实体，A中有多个实体与其发生关联
    ```
## ER图的绘制
