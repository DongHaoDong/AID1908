前请回顾  
1.进程间通信  
* 管道通信 Pipe()  send() recv()
* 消息队列  Queue() q.get() q.put()
* 共享内存 Value() Array()
* 信号量 Semaphore() acquire() release()

2.threading 创建线程
Thread() 创建线程对象
start() 启动线程
join()  回收线程  
3.name is_alive() daemon  
4.自定义线程类:继承Thread重写__init__,run  
5.线程同步互斥  
* 同步互斥方法:
    * Event()
    * wait()
    * set()
    * clear()
    * Lock()
    * acquire()
    * release()
* 死锁:由于上锁造成的程序阻塞
******************************
效率测试:
Single cpu: 7.625521183013916  
Single io: 3.300198554992676  
Process cpu: 2.2472617626190186  
Process io: 0.9062843322753906  
Thread cpu: 7.697145700454712
Thread cpu: 3.533485174179077  
*****************************
练习:根据fork多进程并发网络模型,
完成基于process的多进程并发网络模型
*******************************
ftp文件服务器  
1.技术点确定
* 并发模型:多线程并发
* 数据传输:tcp传输

2.结构设计
* 基本文件操作封装为类

3.功能模块
* 搭建网络通信模型
* 查看文件列表
* 下载文件
* 上传文件
* 客户端退出

4.协议确定
* L 请求文件列表
* Q 退出
* G 下载文件
* P 上传文件 

