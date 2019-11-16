# MySQL高级-Day01回顾
* SQL查询总结
```html
1. select ...聚合函数 from 表名
2. where ...
3. group by ...
4. having ...
5. order by ...
6. limit ...;
```
* 聚合函数(铁三角之一)
```html
avg(...)sum(...)max(...)min(...)count(字段名)# 空值NULL不会被统计
```
* group by (铁三角之二)
```html
给查询结果进行分组
如果select之后的字段名和group by之后的字段不一致，则必须对该字段进行聚合处理(聚合函数)
```
* having语句(铁三角之三)
```html
对查询的结果进行进一步筛选
注意
1.having语句通常和group by语句联合使用，过滤group by语句返回的记录集
2.where只能操作表中实际存在字段，having可操作由聚合函数生成的显示列
```
* distinct
```html
select distinct 字段1,字段2 from 表名;
```
* 查询时做数学运算
```html
select 字段1*2,字段2+5 from 表名;
update 表名 set attack=attack*2 where 条件;
```
* 索引(BTree)
```html
优点：加快数据检索速度
缺点：占用物理存储空间，需要动态维护，占用系统资源
SQL命令运行时间检测
mysql>show variables like "%pro%"；
1. 开启：mysql>set profiling=1;
2. 查看：mysql>show profiles;
3. 关闭：mysql>show profiling=0;
```
* 普通(MUL)、唯一(UNI,字段值不能重复,可为NULL)  
    * 创建
    ```html
    index(字段名),index(字段名)
    unique(字段名),unique(字段名)
    create [unique] index 索引名 on 表名(字段名);
    ```
    * 查看
    ```html
    desc 表名;
    show index from 表名\G;
     Non_Unique:1:index
     Non_Unique:0:unique
    ```
    * 删除
    ```html
    drop index 索引名 on 表名;(只能一个一个删)
    ```
# MySQL高级-Day02笔记
## 外键(foreign key)
* 定义
让当前表字段的值在另一个表的范围内选择
* 语法
```html
foreign key(参考字段名)
references 主表(被参考字段名)
on delete 级联动作
on update 级联操作
```
* 使用规则
1. 主表、从表字段数据类型要一致
2. 主表被参考字段：KEY的一种，一般为主键
* 示例  
    表1、缴费信息表(财务)  
    
    |id|姓名|班级|缴费金额|
    |---|----|----|------|
    |1|唐伯虎|AID1903|300|
    |2|秋香|AID1903|300|
    |3|祝枝山|AID1903|300|
    表2、学生信息表(班主任)--做外键关联

    |stu_id|姓名|缴费金额|
    |------|----|-------|
    |1|唐伯虎|300|
    |2|秋香|300|
    |3|祝枝山|300|
* 删除外键
```html
alter table 表名 drop foreign key 外建名;
```
* 级联操作
```html
cascade
数据级联删除、更新(参考字段)
restrict(默认)
从表有相关记录，不允许主表操作
set null
主表删除、更新，从表相关记录字段值为NULL
```
* 已有表添加外键
```html
alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作
```
## 嵌套查询
定义 



