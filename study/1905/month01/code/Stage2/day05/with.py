"""
with.py
使用with语句打开文件
"""
with open('day05.md',"rb") as f:     # 生成文件对象
    data = f.read()
    print(data.decode())
# with语句块结束 f对象被自动销毁
