'''
位图操作寻找活跃用户
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# user:001      一年中第5天和第200天登录
r.setbit('user:001',4,1)
r.setbit('user:001',199,1)
# user:002      一年中第100天和第300天登录
r.setbit('user:002',99,1)
r.setbit('user:002',299,1)
# user:003      登录了100次以上
for i in range(0,365,2):
    r.setbit('user:003',i,1)
# user:004      登录了100次以上
for i in range(0,366,3):
    r.setbit('user:004',i,1)
# 列表
user_list = r.keys('user:*')
active_users = []
noactive_users = []
# 遍历做统计
for user in user_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_users.append((user.decode(),login_count))
    else:
        noactive_users.append((user.decode(),login_count))
print('活跃用户:',active_users)
print('非活跃用户:',noactive_users)



