"""
数据库处理模块
思路
将数据库操作封装一个类,将dict_server需要的数据库操作
功能分别写成方法,在dict_server中实例化对象,需要什么
直接调用
"""
import pymysql


class Database:
    def __init__(self, host='localhost', port=3306, user='root', password='123456', charset='utf8', database=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        self.database = database
        self.connect_database()  # 连接数据库

    def connect_database(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                  database=self.database, charset=self.charset)

    # 关闭数据库
    def close(self):
        self.db.close()

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 注册操作
    def register(self, name, password):
        sql = "select * from user where name = %s" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False  # 用户存在
        # 插入数据库
        sql = "insert into user (name,password) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, password])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False
