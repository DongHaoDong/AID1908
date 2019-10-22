前情回顾
1.tcp   客户端
    socket --> connect --> send/recv -->close()
2.收发缓冲区：协调收发速度
    粘包：tcp没有消息边界，多次发送内容被一次接收
3.udp   
    服务端：scoket --> bind --> recvfrom/sendto --> close
    客户端：socket --> sendto/recvfrom --> close
4.广播    一端发送多端接收
5.http  协议
    格式：请求格式     响应格式
    请求格式：请求行    GET     /       HTTP/1.1
             请求头    key:value\r\n
                        ......
             空行
             请求体
练习：使用udp完成，客户端不断录入学生信息
     将其发送到服务端，在服务端，将学生信息写入到
     一个文件中，每个学生信息占一行
     信息格式：id name age score
     * id (int)   name(str)     
       age(int)   score(float) 
     