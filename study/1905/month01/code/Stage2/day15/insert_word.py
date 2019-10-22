"""
将单词插入到words单词表
"""
import pymysql
import re

# 打开文件
f = open("dict.txt")

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Dict',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

sql = "insert into words (word,mean) values (%s,%s)"

for line in f:
    # 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()
f.close()
# 关闭游标
cur.close()

# 关闭数据库
db.close()