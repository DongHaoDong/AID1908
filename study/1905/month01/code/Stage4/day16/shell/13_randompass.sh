#!/bin/bash
# 设置变量key，存储密码的所有可能性(密码库),如果还需要其他字符请自行添加其他密码字符
# 使用$#统计密码库的长度
key="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
length=${#key}
# 设置初始密码为空
pass=''
# 循环8次，生成8位随机密码
# 每次都是随机数对密码库的长度取余,确保提取的密码字符不超过密码库的长度
# 每次循环提取一位随机密码，并将该随机码追加到pass变量之后
for i in {1..8}:
do
	index=$[RANDOM%$length]
	pass=$pass${key:$index:1}
done
echo $pass
