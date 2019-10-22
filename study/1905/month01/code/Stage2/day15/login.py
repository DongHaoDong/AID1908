"""
注册登录模拟
"""
"""
mysql.py
pymysql 操作数据库基本流程演示
"""
import pymysql



# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='584023982',database='Student',charset='utf8')

# 获取游标  （操作数据库，执行sql命令）
cur = db.cursor()

# 注册
def register():
    name = input("用户名:")
    password = input("密码：")
    # 判断用户名是否重复
    sql = "select * from users where username='%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql="insert into users (username,userpassword) values (%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True
    except:
        db.rollback()
        return False

# 登录
def login():
    name = input("用户名:")
    password = input("密码：")
    sql = "select * from users where username = '%s' and userpassword = '%s'" %(name,password)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True
while True:
    print("""====================================
        1.注册        2.登录
====================================   
    """)
    cmd = input("输入命令：")
    if cmd == '1':
        # 执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        # 执行登录
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")

    else:
        print("功能正在扩展中")

# 关闭游标
cur.close()

# 关闭数据库
db.close()
