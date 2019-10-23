"""
加密演示
"""
import getpass
import hashlib
pwd = getpass.getpass()
print(pwd)
# 加密处理
hash = hashlib.md5("%*$)@#(*@".encode())
hash.update(pwd.encode())   # 算法 加密
pwd = hash.hexdigest()
print(pwd)