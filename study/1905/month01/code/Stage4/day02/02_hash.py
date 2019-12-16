"""
hash类型操作
"""
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# hset + hget
r.hset('user1','name','bujingyun')
print(r.hget('user1','name'))
# hmset + hmget 返回列表
user_dict = {
    'password':'1423456',
    'gender':'M',
    'girlfriend':'chuchu'
}
r.hmset('user1',user_dict)
print(r.hmget('user1','name','password','gender','girlfriend'))
# hgetall+hkeys+hvals
# hgetall：返回字典
print(r.hgetall('user1'))
# hkeys:返回列表
print(r.hkeys('user1'))
# hvals:返回列表
print(r.hvals('user1'))
# hdel
r.hdel('user1','gender','password')
print(r.hgetall('user1'))