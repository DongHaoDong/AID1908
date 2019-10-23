"""
dict 客户端
功能：根据用户输入，发送请求，得到结果
结构：一级界面 --> 注册  登录  退出
     二级界面 --> 差单词   历史记录    注销
"""
from socket import *
from getpass import getpass  # 运行使用客户端

# 服务端地址
ADDRESS = ('127.0.0.1',8000)
# tcp套接字
s = socket()
s.connect(ADDRESS)

# 注册函数
def do_register():
    while True:
        name = input("User:")
        password01 = getpass()
        password02 = getpass("Again:")
        if password01 != password02:
            print("两次密码不一致!")
            continue
        if ' ' in name or ' ' in password01:
            print("用户名密码不能有空格")
            continue
        message = 'R {} {}'.format(name,password01)
        s.send(message.encode())  # 发送给服务器
        data = s.recv(128).decode()  # 接受结果
        if data == 'OK':
            print("注册成功")
        else:
            print("注册失败")
        return

# 搭建客户端网络
def main():
    while True:
        print("""
        ================== Welcome ================
            1.注册        2.登录        3.退出
        ===========================================
        """)
        cmd = input("输入指令：")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            s.send(cmd.encode())
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print("请输入正确指令:")
if __name__ == "__main__":
    main()

