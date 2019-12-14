import redis
# 创建连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# 通用命令示例
# 列表
key_list = r.keys('*')
print(key_list)
# 遍历列表中的数据
for key in key_list:
    print(key.decode())
# 查看列表类型 b'list'
print(r.type('spider:urls'))
# 返回值:0 | 1
print(r.exists('spider:urls'))
# 设置过期时间
r.expire('spider:urls',5)
# 删除key
r.delete('mylist1','mylist2')
print('mylist1,mylist2删除成功')