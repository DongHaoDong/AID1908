#!/bin/bash

for file in $(ls /etc/*.conf)
do
	md5sum $file >> r2.txt
done
