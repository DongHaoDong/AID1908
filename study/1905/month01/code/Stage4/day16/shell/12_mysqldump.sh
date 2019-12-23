#!/bin/bash

user="root"
passwd="123456"
dbname="mysql"
filename=$(date +%Y-%m-%d)-mysql.sql

# 测试备份目录是否存在,不存在则自动创建该目录
if [ ! -d "/home/tarena/backup" ]; then
	mkdir -p /home/tarena/backup
fi

# 备份
mysqldump -u$user -p$passwd $dbname > /home/tarena/backup/$filename
