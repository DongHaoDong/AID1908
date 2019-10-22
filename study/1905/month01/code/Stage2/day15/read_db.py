"""
read_db.py
pymymql 读操作
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Student',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

# 获取数据库数据
sql = "select Student_Name, age from Student_Class;"
# 执行正确后cur调用函数获取结果
cur.execute(sql)

# 获取一个查询结果
# one_row = cur.fetchone()
# print(one_row)  # 元组

# 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭游标
cur.close()

# 关闭数据库
db.close()
