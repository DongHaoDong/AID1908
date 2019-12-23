#!/bin/bash

read -p "数字已生成,请猜:" you

if [ $you -gt $C ];then
	echo "大"
elif [ $you -lt $C ];then
	echo "小"
else
	echo "对"
fi

