"""
lqueue.py   链式队列
重点代码

思路分析
1.基于链表构建队列模型
2.链表的开端作为队头，结尾作为队尾
3.单独定义队尾标记，避免每次插入数据遍历
4.队头和队尾重叠认为队列为空
"""
# 自定义队列异常
class QueueError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# 实现队列操作
class LQueue:
    def __init__(self):
        # 定义队头和队尾的数形变量
        self.front = self.rear=Node(None)
    # 判断是否为空
    def is_empty(self):
        return self.front == self.rear
    # 入队 rear动
    def enqueue(self,value):
        self.rear.next = Node(value)
        self.rear = self.rear.next
    # 出队 front动
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        # 认为front指向的节点已出队
        self.front = self.front.next
        return self.front.value
if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
