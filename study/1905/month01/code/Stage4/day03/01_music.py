'''
网易云音乐排行榜 - 前三名
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# 有序集合song:rank,参数为字典
r.zadd('song:rank',{'song1':1,'song2':1,'song3':1})
r.zadd('song:rank',{'song4':1,'song5':1,'song6':1})
# 增加分值
r.zincrby('song:rank',50,'song1')
r.zincrby('song:rank',60,'song6')
r.zincrby('song:rank',20,'song5')
# 查看排名 - 前3名:[(b'song6', 61.0), (b'song1', 51.0), (b'song5', 21.0)]
rank_list = r.zrevrange('song:rank',0,2,withscores=True)

i = 1
for rank in rank_list:
    print('第{}名:{}播放次数:{}'.format(i,rank[0].decode(),int(rank[1])))
    i+=1

# 第1名:song6 播放次数:61
# 第2名:song1 播放次数:51
# 第3名：song5 播放次数:21
