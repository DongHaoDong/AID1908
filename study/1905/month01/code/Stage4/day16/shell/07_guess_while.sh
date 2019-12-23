#!/bin/bash

c=$[RANDOM%10000]
while :
do
	read -p "数字已生成,请猜:" you

	if [ $you -gt $c ];then
		echo "大"
	elif [ $you -lt $c ];then
		echo "小"
	else
		echo "对"
		exit
	fi
done			
