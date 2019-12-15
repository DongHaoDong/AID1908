# day01回顾
## Redis回顾
```
1. 基于key-value的菲关系型数据库
2. 基于内存存储，速度很快
3. 基于内存存储，经常当做缓存型数据库使用，常用信息缓存在redis数据库中
```
## 五大数据类型
```
1. 字符串类型(string)
2. 列表(list)
3. 哈希(hash)
4. 集合类型(set)
5. 有序集合类型(sorted set)
```
### 字符串类型
```
# 设置key相关操作
1. set key value
2. set key value nx
3. mset k1 v1 k2 v2 k3 v3
4. expire key 5
5. pexpire key 5
6. tll key
7. persist key
# 获取key相关操作
8. get key
9. mget k1 k2 k3
10. strlen key
# 数字类型相关操作
11. incrby key 步长 
12. decrby key 步长 
13. incr key
14. decr key
15. incrbyfloat key number
```
### 列表类型
```
# 插入元素相关操作
1. LPUSH key value1 value2
2. RPUSH key value1 value2
3. RPOPLPUSH source destination
4. LINSERT key after|before value newvalue
# 查询相关操作
5. LRANGE key start stop
6. LLEN key
# 删除相关操作
7. LPOP key
8. RPOP key
9. BLPOP key timeout
10. BRPOP key timeout
11. LREM key count value
12. LTRIM key start stop
# 修改制定元素相关操作
13. LSET key index newvalue
```
* 思考：
Reids列表如何当做共享队列来使用
```
# 同学您好，你还记得小米应用商店爬取URL地址的案例吗
1. 生产者消费者模型
2. 生产者进程在列表中 LPUSH | RPUSH 数据，消费者进程在列表中 BRPOP | BLPOP 数据
```
Python与Redis交互注意
```
r.set('name','Tom',ex=5,nx=True)

r.mset({'user001:name':'Tom','user001:300':'25'})
```
# day02
## 位图操作bitmap
* 定义
```
1. 位图不是真正的数据类型，它是定义在字符串类型中
2. 一个字符串类型的值最多能存512m字节的内容，位上限:2^32
# 1MB = 1024KB
# 1KB = 1024Byte(字节)
# 1Byte = 8bit(位)
```
* 强势点
```
可以实时的进行统计，极其节省空间。官方模拟1亿2千8百万用户的模拟环境下，在一台MacBookPro上，典型的统计如'日用户数'的时间消耗小于50ms,占用16mb内存
```
* 设置某一位上的值(setbit)
```
# 设置某一位上的值(offset是偏移量,从0开始)
setbit key offset value
# 获取某一位上值
GETBIT key offset
# 统计键所对应的值中有多少个1,start和end是字节
BITCOUNT key [start end] 
```
* 示例
```
# 默认扩展位以0填充
127.0.0.1:6379> set mykey ab
OK
127.0.0.1:6379> get mykey
'ab'
127.0.0.1:6379> SETBIT mykey 0 1 
(integer) 0
127.0.0.1:6379> get mykey 
'\xelb'
127.0.0.1:6379>
```
* 获取某一位上的值  
GETBIT key offset  
```
127.0.0.1:6379> get mykey 3
(integer) 0
127.0.0.1:6379> get mykey 0
(integer) 1
127.0.0.1:6379>
```
* bitcount
统计键所对应的值有多少个1
```
127.0.0.1:6379> SETBIT user001 1 1
(integer) 0
127.0.0.1:6379> set user001 30 1
(integer) 0
127.0.0.1:6379> bitcount user001
(integer) 2
127.0.0.1:6379>
```
* 应用场景
```
# 网站用户的上线次数统计(寻找活跃用户)
    用户名为key,上线的天数作为offset，上线设置为1
# 示例
    用户名为user1:login的用户，今年第1天上线，第30天上线
    SETBIT user1:login 0 1
    SETBIT user1:login 29 1
    BITCOUNT user1:login 
```
* 代码实现
```
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
```
# Hash散列数据类型
* 定义
```
1. 由field和关联的value组成的键值对
2. field和value是字符串类型
3. 一个hash中最多包含2^32-1个键
```
* 优点
```
1. 节约内存空间
2. 每创建一个键，它都会为这个键存储一些附加的管理信息(比如这个键的类型，这个键最后一次被访问的时间等)
3. 键越多，redis数据库在存储附件管理信息方面消耗内存越多，花在管理数据库键上的cpu也会越多
```
* 缺点(不适合hash情况)
```
1. 使用二进制位操作命令:SELECT GETBIT BIT COUNT等，如果想使用这些操作，只能用字符串键
2. 使用过期键功能:键过期功能只能对键进行过期操作，而不能对散列的字段进行过期操作
```
* 基本命令操作
```
# 1. 设置单个字段
HSET key field value
HSETNX key field value
# 2. 设置多个字段
HMSET key field value field value
# 3. 返回字段个数
HLEN key
# 4. 判断字段是否存在(不存在返回0)
HEXISTS key field
# 5. 返回字段值
HGET key field
# 6. 返回多个字段值
HMGET key field field
# 7 返回所有的键值对
HGETALL key
# 8. 返回所有字段名
HKEYS key
# 9. 返回所有值
HVALS key
# 10. 删除指定字段
HDEL key field
# 11. 在字段对应值上进行整数增量运算
HINCRBY key field increment
# 12. 在字段对应智商进行浮点数增量运算
HINCRBYFLOAT key field increment
```
* hash和python交互
```
# 1. 更新一条数据的属性，没有则新建
hset(key,field,value)
# 2. 读取这条数据的指定属性，返回字段类型
hget(key,field)
# 3. 批量更新数据(没有则新建)属性,参数为字典
hmset(key,mapping)
# 4. 批量读取数据(没有则新建)属性
hmget(key,fields)
# 5. 获取这条数据的所有属性和对应的值，返回字典类型
hgetall(key)
# 6. 获取这条数据的所有属性名，返回列表类型
hkeys(key)
# 7. 删除这条数据的指定属性
hdel(key,*fields)
```
* python代码hash散列
```
```
* 应用场景:微博好友关注
```
1. 用户ID为key,Field为好友ID,value为关注时间
    key         field       value
 user:1000000   user:606    20190520
                user:605    20190521
2. 用户维度统计
    统计数包括:关注数、粉丝数、喜欢商品数、发帖数
    用户为key,不同维度为field,value为统计数
    比如关注了5人
   key          field       value
   user:10000   fans          5
                ties          10
        HSET user:1000 fans 5
        HINCRBY user:1000 fans 1
```
## 应用场景:redis+mysql+hash组合使用
* 原理
```
用户想要查询个人信息
1. redis缓存中查询个人信息
2. redis中查询不到，到mysql中查询，并缓存到redis
3. 再次查询个人信息
```
* 代码实现
```
```
* mysql数据库中数据更新信息后同步到redis缓存
用户修改个人信息时，要将数据同步到redis缓存


