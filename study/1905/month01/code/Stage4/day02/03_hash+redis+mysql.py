'''
hash+redis+mysql组合使用
'''
import redis
import pymysql

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='584023982',
    database='userdb',
    port=3306,
    charset='utf8'
)
cursor = db.cursor()

# 1. 用户要查询的用户名
# 2. 先到redis中查询
# 3. redis中如果没有，到mysql中查询
username = input("请输入用户名:")
result = r.hgetall(username)
# redis中存在数据
if result:
    print('redis',result)
else:
    # 1. mysql中查询 -返给用户
    sel = 'select age,gender,score from user where name=%s'
    cursor.execute(sel,[username])
    userinfo = cursor.fetchall()
    # userinfo:空元组
    if not userinfo:
        print('用户不存在')
    else:
        print('mysql:',userinfo)
        # userinfo: ((25,'M',90),)
        # 2. 缓存到redis中一份，设置过期时间30秒
        user_dict = {
            'age':userinfo[0][0],
            'gender':userinfo[0][1],
            'score':userinfo[0][2]
        }
        r.hmset(username,user_dict)
        # 设置过期时间30秒
        r.expire(username,30)

# hash
# key field value
# niefeng age gender score
