import redis
import pymysql


class Update(object):
    def __init__(self):
        self.db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='584023982',
        database='userdb',
        port=3306,
        charset='utf8'
    )
        self.cursor = self.db.cursor()
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    # 更新mysql表记录
    def update_mysql(self,score,username):
        upd = 'update user set score=%s where name=%s'
        try:
            # code:0或者1,几行受到了影响
            code = self.cursor.execute(upd,[score,username])
            # code为1：说明新成绩和原成绩不一样
            if code == 1:
                self.db.commit()
                return True
        except Exception as e:
            self.db.rollback()
            print('Failed',e)
    # 同步到redis数据库
    def update_redis(self,username,score):
        result = self.r.hgetall(username)
        # 存在，更新score字段的值
        if result:
            self.r.hset(username,'score',score)
        else:
            # 到mysql中查询最新数据，缓存到redis中
            self.select_mysql(username)
    # mysql查询数据 + 更新到redis数据库
    def select_mysql(self,username):
        sel = 'select age,gender,score from user where name=%s'
        self.cursor.execute(sel,[username])
        result = self.cursor.fetchall()
        # 缓存到redis数据库
        user_dict = {
            'age': result[0][0],
            'gender': result[0][1],
            'score': result[0][2]
        }
        self.r.hmset(username,user_dict)
        self.r.expire(username,60)

    def main(self):
        username = input('请输入用户名:')
        new_score = input('请输入新成绩:')
        if self.update_mysql(new_score,username):
            self.update_redis(username,new_score)
        else:
            print('更改信息失败')

if __name__ == '__main__':
    syn = Update()
    syn.main()