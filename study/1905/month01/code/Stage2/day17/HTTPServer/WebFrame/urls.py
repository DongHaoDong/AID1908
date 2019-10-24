"""
可以通过客户端任意的数据访问
"""
from views import *

urls = [
    ("/time",show_time),
    ("/hello",hello),
    ("/bye",bye)
]
