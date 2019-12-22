# Linux
## 常用的Linux操作系统
```
RedHat(红帽):6.5,7
CentOS:6.5,7
Ubuntu:16.04,18.04
```
## 远程连接工具-xshell
```
# 1. 定义
xshell:安装终端模拟软件
# 2. 使用
文件-新建-输入服务器IP地址-输入用户名-输入密码-确认连接
# 3. 文件互传
sudo apt-get install lrzsz
Windows -> Linux:rz
Linux -> Windows:sz filename 
```
## 默认已熟练使用的Linux命令
```
1. pwd
2. cd       -- cd .. cd
3. ls       -- ll
4. mkdir -p
5. touch
6. tar 
    tar -zcvf xxx.tar.gz dir1
    tar -zxvf xxx.tar.gz
    tar -xf xxx.tar.gz
    tar xf xxx.tar.gz
    unzip xxx.zip
7. cp       --cp -r # -r选项递归复制，复制非空文件夹
8. mv
mv dir1 /home/tarena/
mv dir1 new_dir1
```
## 常用命令
```
1. ifconfig
    查看IP地址和MAC地址
    windows中命令为:ipconfig或者ipconfig /all
    # ubuntu18.04不能使用ifconfig
    sudo apt-get install net-tools
2. ping IP/域名 [-c n]
    测试网络连通性，-c指定连接次数
3. nslookup 域名
    解析域名对应的ip地址
4. ls -lh file|directory
    显示文件权限及详细信息，h选项提供易读容量单位
    -rw-r--r-- tarena tarena
    分三组:所有者权限 所属组用户权限 其他用户权限
    r - 读（4）
    w - 写（2）
    x - 可执行（1）
    前三位:所有者(tarena这个用户)rw-
    中三位:所属组其他用户(用户tarena2对文件的权限)r--
    尾三位:其他组其他用户(用户develop1对文件的权限)r--
    # 777 rwxrwxrwx
    # 666 rw-rw-rw-
    # 644 rw-r--r--
5. tar -zcvf filename.tar.gz file1 file2 directory3
    将文件|目录打包并压缩
6. tar -zxvf filename.tar.gz [-C path]
    解压缩，默认解压到当前路径，-C可指定路径
7. ps -aux
    显示进程命令(包括PID号) ps -aux | grep 'mysql'
8. kill PID
    杀死某个进程
    eg:ps -aux | grep 'mysql'
    sudo kill PID号
9. chmod 权限 file
    给文件制定或者新增某种权限
    chmod 777 文件名
    chmod 664 文件名
    rw-r--r--
    chmod u+x 文件名 # 文件所有者增加x权限(user)
    chmod g+w 文件名 # 同组其他用户增加w权限(group)
    chmod o-r 文件名 # 其他组其他用户减r权限(other)
    chmod a+x 文件名 # 给所有权限增加x权限(all)
    
10. chown user:group file
    更改属主和属组
    eg:chown root:root file
11. find path -name filename
    在某个路径下查找某个文件
    eg:find /home/tarena/ -name '*.avi'
12. ssh user@IP
    远程连接到服务器
    eg:ssh tarena@192.168.203.129
13. scp file user@IP:绝对路径
    本地文件复制到远程
    eg:scp python.tar.gz tarena@192.168.203.129:/home/tarena/    
```
## vi及vim使用
```
文本编辑器,vim是vi的升级版
# 使用流程
1. vi filename
初始(不能编辑,预览模式) -> 按a(可编辑，插入模式) -> 编辑内容 -> 按ESC,然后shift+:(命令行模式) -> 输入wq!(保存并退出)、或q!(不保存退出)
# 练习
1. 打开一个文件,写入你最喜欢的一首诗,保存退出
2. cat 文件名

# 常用
1. 查找
    浏览模式 -> 输入 / -> 输入查找内容 -> Enter(n表示下一个，shift+n表示上一个)
2. 复制+删除+粘贴+撤销
    yy:复制光标所在行(2yy复制两行内容)
     p:粘贴
     dd:删除(剪切)光标所在行(3dd删除(剪切)三行内容)
     u:撤销
# 光标的跳转(浏览模式)
    行首:home
    行尾:end
    全文的首航:gg
    全文的最后一行:G
    全文的12行:12G
```
**练习**
```
1. 在用户主目录下新建目录(mkdir):你的名字(比如:董浩东)
# mkdir 董浩东
2. 在目录董浩东中新建song.txt(可使用touch命令，或者直接使用vim)
# vim song.txt
3. 在song.txt中写入一首你最喜欢的一首诗,保存并退出
# ESC->:wq
4. 把/etc/passwd文件拷贝到董浩东目录一份(cp命令)
# sudo cp /etc/passwd /home/tarena/董浩东/
5. 在/home/tarena/董浩东/passwdwe文件中筛选tarena用户的信息(grep命令)
# grep 'tarena' ~/董浩东/passwd
6. 查看passwd文件的权限,并将其权限修改为所有用户都可读可写但不可执行(chmod命令)
# sudo chmod 666 ~/董浩东/passwd
7. 将董浩东目录打包压缩，董浩东-你的名字.tar.gz
# tar -zcvf 董浩东-董浩东.tar.gz 董浩东
8. 将此压缩吧远程复制到主讲机 | 同坐 计算机的电脑上
scp 董浩东-董浩东.tar.gz tarena@192.168.203.129:/home/tarena/homework
```
## Linux命令-Go on
```
# 14.管道操作
    将前面命令的输出，传递给后面命令，作为后面命令的参数
    查看 /etc/passwd文件的第6-10行? -cat、head、tail
    # cat /etc/passwd | head -10 |tail -5
    # head -10 /etc/passwd | tail -5
# 15.统计目录总共的占用空间大侠
    du -sh 目录
# 16.查看磁盘使用情况(根分区使用情况)
    df -h
# 17.常见通配符使用
    *:任意多个字符
    ?:单个字符
    eg1:rm -rf /home/tarena/test/*
    eg2:ls *.jpg
# 18.重定向:将前面命令的输出,写入到文本文件中
    >:覆盖重定向
    >>:追加重定向
# 19.创建用户(会创建同名组)
    useradd username
# 20.设置密码
    sudo passwd 用户名
# 21.删除用户
    userdel
    -r:递归删除,删除用户的家目录以及用户的邮件文件
```
## raid0 raid1 raid5的区别
```
# 1.什么是raid?
由一系列硬盘组成的阵列，简单说:一个服务器有10个硬盘，你如何保证坏掉一个硬盘后数据不丢，业务不断
# raid分类:raid0、raid1、raid5
raid0
    1.特点:数据分散存储在多个硬盘
    2.优点:读写并发，存储超快，提升数倍
    3.缺点:一旦一个磁盘挂掉，则损坏全部数据
raid1
    1.特点:数据分别写入两个磁盘(写了两份)
    2.优点:实现了数据备份
    3.缺点:磁盘使用率只能到50%
raid5
    1. 特点:提供热备份实现故障恢复
    2. 优点:只损坏1块磁盘，数据不会损坏
    3. 缺点:同时损坏2块硬盘，数据损坏
```
## Linux-Go on
```
# 22.统计文件的行数
    wc -l
        eg1:wc -l /etc/passwd
# 23.对文件中内容进行排序
    sort 文件名
# 24.去除重复行，并统计每行出现的次数(相邻行)
    uniq -c
    sort 文件名 | uniq -C
```
## 周期性计划任务
```
# 1.进入周期性计划任务
crontab -e(首次进入按2 - 找vim)
# 设置周期性计划任务
* * * * * :五个*号代表 分 时 日 月 周
0 2 * * * :每天凌晨两点
分:0-59
时:0-23
日:1-31
月:1-12
周:0-6
# 开始设置
1. '*'代表所有可能值
2. ','指定多个时间点
3. '/'指定时间间隔频率
4. '-'指定一个时间段
# 示例
1. 每月的1日和5日两天: * * 1,5 * *
2. 每10分钟: */10 * * * *
3. 0点-6点每小时执行: 0 0-6/1 * * *
4. 每分钟执行: * * * * *
# 练习
1. 每小时的第3分钟和第15分钟执行
    3,15 * * * *
2. 每周六、周日的0点执行一个01.py文件
    0 0 * * 6,0
6. 每天18:00到23:00之间每小时执行01.py文件
    0 18-23/1 * * *
```
## 文本处理工具 - awk
### 语法格式
```
awk 选项 '动作' 文件列表
```
### 常用方式
```
Linux命令 | awk 选项 '动作'
```
### 使用方法
```
# 示例
awk '{print "abc"}' ip.txt
# 思考:这个会输出什么?
    df -h | awk '{print $1}'
# -F:指定分隔符
awk -F ":" '{print $2}' # 显示: 分隔后的第2列
# 示例:提取根分区的使用量
df -h | head -4 | tail -1 | awk '{print $5}' | awk -F '%' {print $1} 
# 练习
输出本机的IP地址
ifconfig | head -2 | tail -1 | awk '{print $2}'
```
### 作业
```
# nginx的访问日志目录
/var/log/nginx/access.log
问题1:把访问过自己的IP地址输出
    # awk '{print $1}' access.log
问题2:统计有多少个IP访问过我
    # awk '{print $1}' access.log | sort | uniq | wc -l
问题3:统计每个IP地址的访问次数,输出前10个访问量最大的用户IP
    # awk '{print $1}' access.log | sort | sort -rn -k 1 | head -10
```
### grep命令之正则表达式
```
# 正则表达式元字符集 - 使用grep命令
^ : 以...开头
$ : 以...结尾

```

