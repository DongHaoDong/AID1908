#!/bin/bash 

for i in {1..254}
do
	# /dev/null为黑洞,不想要的输出放在里面
	ping -c 2 192.168.43.$i &> /dev/null
	# $?返回上一条命令的执行状态
	if [ $? -eq 0 ];then
		echo "192.168.43.$i is up"
	else
		echo "192.168.43.$i is down"
	fi
done
