"""
mysql.py
pymysql 操作数据库基本流程演示
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Student',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

# 执行数据库
sql = "insert into Student_Class values (11,'Test',21,'W',76.5,'2019-10-21');"

# 执行sql命令
cur.execute(sql)

# 将写操作提交，多次写操作一同提交
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()
