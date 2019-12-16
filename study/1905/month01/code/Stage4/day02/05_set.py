import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# python操作set
r.delete('myset1')
r.sadd('myset1','A','B')
# 返回类型：集合
print(r.smembers('myset1'))
print(r.scard('myset1'))
# ismember 返回值： True | False
print(r.sismember('myset1','C'))

# 交集+并集
r.sadd('myset2','A','B','C')
r.sadd('myset3','B','C','D')
print(r.sinter('myset1','myset2','myset3'))
# {b'B', b'A', b'C', b'D'}
forcus_set = r.sunion('myset1','myset2','myset3')
# 定义空集合
result = set()
for focus in forcus_set:
    focus = focus.decode()
    result.add(focus)
print(result)
# {'B', 'A', 'C', 'D'}
