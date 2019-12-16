'''
使用executemany()方法插入2条记录
'''
import pymysql

# 创建2个对象
db = pymysql.connect('127.0.0.1','root','584023982','maoyandb',charset='utf8')
cursor = db.cursor()

# 执行sql命令
ins = 'insert into filmtab values(%s,%s,%s)'
film_list = [('月光宝盒','周星驰','1993'),('大圣娶亲','周星驰','1933')]
cursor.executemany(ins,film_list)
# 提交到数据库执行
db.commit()
cursor.close()
db.close()