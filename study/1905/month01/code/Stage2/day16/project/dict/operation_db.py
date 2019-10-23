"""
数据库处理模块
思路
将数据库操作封装一个类,将dict_server需要的数据库操作
功能分别写成方法,在dict_server中实例化对象,需要什么
直接调用
"""
import pymysql
import hashlib

SALT = "!%)@(%)@*#@"  # 盐


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
        sql = "select * from user where name = '%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False  # 用户存在
        # 密码加密存储处理
        hash = hashlib.md5((name + SALT).encode())
        hash.update(password.encode())  # 算法 加密
        password = hash.hexdigest()  # 加密后的密码
        # 插入数据库
        sql = "insert into user (name,password) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, password])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 登录处理
    def login(self, name, password):
        # 密码加密存储处理
        hash = hashlib.md5((name + SALT).encode())
        hash.update(password.encode())  # 算法 加密
        password = hash.hexdigest()  # 加密后的密码

        # 进行数据库查找
        sql = "select * from user where name='%s' and password='%s'" % (name, password)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 有数据则允许登录
        if r:
            return True
        else:
            return False

    # 查单词
    def query(self,word):
        sql = "select mean from words where word='%s'"%(word)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 如果找到 r --> (mean)
        if r:
            return r[0]

    # 插入历史记录
    def insert_hist(self,name,word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

