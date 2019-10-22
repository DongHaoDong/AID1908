"""
sequeue.py  队列的顺序存储

思路分析：
1.基于列表完成数据存储
2.通过封装规定数据操作
3.先确定列表的哪一段作为队头
"""
# 自定义队列异常
class QueueError(Exception):
    pass
# 队列操作
class SQueue:
    # 初始化
    def __init__(self):
        self._elements = []
    # 判断队列是否为空
    def is_empty(self):
        return self._elements == []
    # 入队 列表尾部定义为队尾
    def enqueue(self,value):
        self._elements.append(value)
    # 出队 列表的第一个元素
    def dequeue(self):
        if not self._elements:
            raise QueueError("Queue is empty")
        return self._elements.pop(0)
if __name__ == "__main__":
    sq = SQueue()
    for i in range(10):
        sq.enqueue(i)
########  实现队列翻转  ##########
    from sstack import *
    st = SStack()
    # 循环 出队入栈
    while not sq.is_empty():
        st.push(sq.dequeue())
    # 循环出栈入队
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())
