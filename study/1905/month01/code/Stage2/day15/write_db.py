"""
write_db.py
pymysql写操作(insert delete update)
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Student',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

# 写操作数据库
try:
    # 写sql语句

    # 插入操作
    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score:")
    # 将变量插入到sql语句合成最终操作语句
    # sql = "insert into Student_Class (Student_Name,age,score) values ('{}',{},{})".format(name,age,score)
    # print(sql)
    # sql = "insert into Student_Class (Student_Name,age,score) values (%s,%s,%s)"
    # 可以使用列表直接给sql语句的values传值
    # cur.execute(sql,[name,age,score])  # 执行

    # 修改操作
    # sql = "update Interest_Class set price = 11800 where Class_Name = 'LiuFan'"
    # cur.execute(sql)

    # 删除操作
    sql = "delete from Student_Class where score<90"
    cur.execute(sql)

    db.commit()  # 提交
except Exception as e:
    # 退回到commit执行之前的数据库状态
    db.rollback()
    print(e)

# 关闭游标
cur.close()

# 关闭数据库
db.close()