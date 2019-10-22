前情回顾  
1.数据库基本概念
* 为什么用数据库
* 什么是数据库
* 数据库简单分类
    * 关系型 & 非关系型
    * 开源  &  非开源
    * 大型  &  中型  &  小型
* 关系型数据库组成结构
数据元素 --> 记录 --> 数据表 --> 数据库

数据库 (database)
数据表  (table)
字段    (column)
记录    (row)
主键:   不重复不能为空  (primary key)
2.mysql 关系型   开源  C/C++  安装
3.SQL语句
* 数据库操作
    * 创建数据库 create database [db_name];
    * 查看数据库 show databases;
    * 查看当前数据库 select databases();
    * 查看数据库创建信息 show create database [db_name];
    * 切换数据库  use [db_name];
    * 删除数据库  drop database [db_name];
* 数据表操作:
    * 查看数据表 show tables;
    * 创建数据表 create table [tb_name] (column1 type,...),...
        * 字段描述
            primary key
            unsigned
            not null
            default
        * 数据类型
            * 数字 (正数,小数,布尔)
            * 字符 (char,varchar,blob,text,enum,set)
            * 时间日期  
    * desc [tb_name];查看数据表信息
    * show create table [tb_name];查看数据表创建信息
    * drop table [tb_name];删除数据表
*增删改查
insert into [tb_name] (column,..) values (value)
delete from [tb_name] where ...
update [tb] set ... where ...
select [column,...] from [tb_name] where ...
where 字句: 算数    逻辑      比较      位运算
* 表结构
alter table [tb_name ] add
alter table [tb_name ] drop
alter table [tb_name ] modify
alter table [tb_name ] change
alter table [tb_name ] rename


                      
        
