#!/bin/bash

echo "+-----------------------------+"
echo "|      Welcome(q to quit)     |"
echo "+-----------------------------+"

read -p "请输入一个字符:" char

if [ ${#char} -ne 1 ];then
	echo "$char不是1个字符！！"
	exit
elif [ $char == "q"  ];then
	echo "程序退出"
	exit
fi

case $char in
[a-z]|[A-Z])
	echo "字母"
	;;
[0-9])
	echo "数字"
	;;
*)
	echo "其他字符"
	;;
esac
