#!/bin/bash

sumn(){
	echo $[n1+n2]
}

subn(){
	echo $[n1-n2]
}

read -p "First:" n1
read -p "Second:" n2
read -p "Operation(+|-):" op

case $op in
"+")
	sumn
	;;
"-")
	subn
	;;
*)
	echo "Invalid"
	;;
esac
