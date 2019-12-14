import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# 常见附五的端口号
# 1. mysql -> 3306
# 2. oracle -> 1521
# 3. redis -> 6379
# 4. mongodb -> 27017
# 5. http -> 80
# 6. https -> 443
# 7. ssh -> 22 远程连接服务
# 8. telnet -> 23 远程连接服务
# 5. ftp -> 21 远程连接服务

# 列表操作
# ['LiuFan','ZhangLele','ChenHuan','YangYueyue','XueChen','PengLong']
r.rpush('donghaodong:friend','LiuFan','ZhangLele','ChenHuan','YangYueyue','XueChen')
r.rpush('donghaodong:friend','PengLong')
# 在YangYueyue后面添加WangYu
r.linsert('donghaodong:friend','after','YangYueyue','WangYu')
# 打印长度
print(r.llen('donghaodong:friend'))
# 查看所有元素 - 列表
print(r.lrange('donghaodong:friend',0,-1))
# 弹出一个元素
print(r.rpop('donghaodong:friend'))
# 保留指定范围内元素
r.ltrim('donghaodong:friend',0,3)
# 阻塞弹出
while True:
    # 三秒钟后无元素弹出返回None
    result = r.brpop('donghaodong:friend',3)
    if result:
        print(result)
    else:
        break
r.expire('donghaodong:friend',10)