"""
save_image.py
二进制文件的存储
"""
import pymysql
# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Student',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

# # 存储图片
# with open('file.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update student_class set images = %s where Student_Name='ZhangLeLe';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select images from Student_Class where Student_Name='LiuFan'"
cur.execute(sql)
data = cur.fetchone()
with open('girl.jpg','wb') as f:
    f.write(data[0])


# 关闭游标
cur.close()
# 关闭数据库
db.close()