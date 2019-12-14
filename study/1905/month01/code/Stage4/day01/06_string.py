import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# python操作string
r.set('user001:name','donghaodong')
m_dict = {
    'user001:age':21,
    'user001:gender':'M'
}
r.mset(m_dict)
# b'donghaodong'
print(r.get('user001:name'))
# 列表:{'34','M'}
print(r.mget('user001:age','user001:gender'))
print(r.strlen('user001:name'))
# 数值操作
r.incr('user001:age',1)
r.decr('user001:age',1)
r.incrby('user001:age',3)
r.decrby('user001:age',3)
r.incrbyfloat('user001:age',1.5)
r.incrbyfloat('user001:age',-1.5)
print(r.get('user001:age'))