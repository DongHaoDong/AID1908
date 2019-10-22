练习:  
1.创建数据库grade  
create database grade character set utf8
2.数据库中创建表student  
create table student
(
    id int primary key auto_increment,
    name varchar(32) not null,
    age int not null,
    score float default 0.0,
    hobby set('football','computer','running','basketball'),
    comment text
);
3.表字段如下  
id name age ,hobby score comment
4.插入若干数据
age 4 -- 16
score 0 -- 100
hobby: football computer running basketball
insert into student values(1,'YangYueYue',4,80.5,'running,computer','继续加油,你是最棒的!'),(2,'DongHaoDong',12,90.5,'computer,running','多才多艺,艺高人胆大'),(3,'XueChen',15,88.5,'basketball,running','英雄出少年,前途无量'),(4,'DuYunYang',16,36.5,'basketball,football','成绩很差,叫家长');
5.查找
* 查找所有年龄不到10岁,或者大于14岁的同学
select * from student where age < 10 or age > 14;
* 查找兴趣爱好中包含computer的同学
select * from student where find_in_set('computer',hobby);
* 查找年龄大于等于15,又喜欢足球的同学
select * from student where find_in_set('football',hobby) and age >= 15;
* 查找不及格兴趣爱好又不为空的同学
select * from student where hobby is not null and score < 60;
* 查找成绩大于90分的所有同学,只看姓名和成绩
select name,score from student where score > 90;
