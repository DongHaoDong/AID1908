"""
死锁
"""
from time import sleep
from threading import Thread,Lock
# 交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id # 用户
        self.balance = balance # 存款
        self.lock = lock # 锁
    # 取钱
    def withdraw(self,amount):
        self.balance -= amount
    # 存钱
    def deposit(self,amount):
        self.balance += amount
    # 查看余额
    def get_balance(self):
        return self.balance
# 产生两个账户
Tom = Account('Tom',5000,Lock())
Alex = Account('Alex',8000,Lock())
# 转账过程
def transfer(from_,to,amount):
    if from_.lock.acquire(): # 锁住子集的账户
        from_.withdraw(amount) # 账户减少
        sleep(0.5)
        if to.lock.acquire(): # 锁住对方账户
            to.deposit(amount) # to账户加钱
            to.lock.release() # to解锁
        from_.lock.release() # from解锁
    print("{}给{}转账{}".format(from_.id,to.id,amount))
t1 = Thread(target=transfer,args=(Tom,Alex,2000))
t2 = Thread(target=transfer,args=(Alex,Tom,3500))
t1.start()
t2.start()
t1.join()
t2.join()