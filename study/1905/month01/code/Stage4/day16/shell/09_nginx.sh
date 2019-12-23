#!/bin/bash

read -p "请选择操作(start|stop|restart):" operation

case $operation in
"start")
	sudo /etc/init.d/nginx start
	;;
"stop")
	sudo /etc/init.d/nginx stop
	;;
"restart")
	sudo /etc/init.d/nginx restart
	;;
*)
	echo "Usage: nginx {start|stop|restart}"
	;;
esac
