"""
linklist.py
功能：实现单链表的构建和功能操作
重点代码
"""

# 创建节点类
class Node:
    """
    思路：将自定义的类视为节点的生成类,实例对象中包含数据部分和指向下一节点的next
    """
    def __init__(self, value, next=None):
        self.value = value  # 有用数据
        self.next = next    # 循环下一个节点关系

# 做链表的各种操作
class LinkList:
    """
    思路：单链表类，生成对象可以进行增删改查操作
        具体操作通过调用具体方法完成
    """
    def __init__(self):
        """
        初始化链表，编辑一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)
    # 通过list_为链表添加一组节点
    def init_list(self,list_):
        p = self.head   # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next
    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.value)
            p = p.next  # p向后移动
    # 判断链表是否为空
    def is_empty(self):
        if self.hand.next is None:
            return True
        else:
            return False
    # 清空链表
    def clear(self):
        self.head.next = None
    # 尾部插入节点
    def append(self,value):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)
    # 头部插入节点
    def head_insert(self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
    # 在指定位置插入节点
    def insert(self,index,value):
        p = self.head
        for i in range(index):
            # 超出位置最大范围结束循环
            if p.next is None:
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node
    # 删除节点
    def delete(self,value):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next and p.next.value != value:
            p = p.next
        if p.next is None:
            raise ValueError("value not in linklist")
        else:
            p.next = p.next.next
    # 获取某个节点值,传入节点位置获取节点值
    def get_index(self,index):
        if index < 0:
            raise IndexError("list index out range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out range")
            p = p.next
        return p.value
