'''
京东手机畅销榜
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

day01_dict = {
    'huawei':5000,
    'oppo':4000,
    'iphone':3000
}
day02_dict = {
    'huawei':5200,
    'oppo':4200,
    'iphone':3200
}
day03_dict = {
    'huawei':5300,
    'oppo':4300,
    'iphone':3300
}
r.zadd('mobile:001',day01_dict)
r.zadd('mobile:002',day02_dict)
r.zadd('mobile:003',day03_dict)
# 求并集：mobile:001-003,多个集合为元组
r.zunionstore(
    'mobile:001-003',
    ('mobile:001','mobile:002','mobile:003'),
    aggregate='max'
)
# 求排名:zrevrange:[(b'huawei',5300.0),(),()]
rank_list = r.zrevrange('mobile:001-003',0,2,withscores=True)
# 打印输出
i = 1
for rank in rank_list:
    print('第{}名:{}销量:{}'.format(i,rank[0].decode(),int(rank[1])))
    i += 1