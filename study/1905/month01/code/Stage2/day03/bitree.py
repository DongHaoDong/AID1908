"""
bitree.py   二叉树的简单实践

思路分析：
1.使用链式存储，一个Node表示一个树的节点
2.节点考虑使用两个属性变量分别表示左连接和右连接
"""
from sequeue import *
# 二叉树节点
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
# 二叉树遍历类
class Bitree:
    def __init__(self,root=None):
        self.root = root
    # 先序遍历
    def preOrder(self,node):
        if node is None:    # 终止条件
            return
        print(node.value,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
    # 中序遍历
    def inOrder(self,node):
        if node is None:    # 终止条件
            return
        self.inOrder(node.left)
        print(node.value,end=" ")
        self.inOrder(node.right)
    # 后续序遍历
    def rearOrder(self, node):
        if node is None:  # 终止条件
            return
        self.rearOrder(node.left)
        self.rearOrder(node.right)
        print(node.value,end=" ")
    # 层次遍历
    def levelOrder(self,node):
        """
        让初始节点先入队，谁出队就遍历谁，并且让它的左右孩子分别入队，直到队列为空
        """
        sq = SQueue()
        sq.enqueue(node)    # 初始节点入队
        while not sq.is_empty():
            node = sq.dequeue()
            # 打印出队元素
            print(node.value,end = " ")
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

if __name__ == "__main__":
    # B F G D I H E C A
    # 根据后序遍历构建二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D',f,g)
    i = Node('I')
    h = Node('H')
    e = Node('E',i,h)
    c = Node('C',d,e)
    a = Node('A',b,c)   #  树根
    # 将a作为遍历的起始位置
    bt = Bitree(a)

    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.rearOrder(bt.root)
    print()
    bt.levelOrder(bt.root)

