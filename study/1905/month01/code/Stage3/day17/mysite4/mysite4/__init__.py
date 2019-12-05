# file:mytite4/ __init__.py

import pymysql

# 让Django用pymysql对mysql服务器进行操作
pymysql.install_as_MySQLdb()