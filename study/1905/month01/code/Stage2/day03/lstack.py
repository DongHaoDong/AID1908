"""
lstack.py   栈的链式栈
重点代码

思路分析：
1.源于链表结构
2.封装栈的操作方法(入栈，出栈，栈空，栈顶元素)
3.链表的开头作为栈顶?(不用每次遍历)
"""
# 自定义异常类
class StackError(Exception):
    pass
# 节点类
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None
    # 判断是否为空
    def is_empty(self):
        return self._top is None
    # 入栈
    def push(self,value):
        self._top = Node(value,self._top)
    # 出栈
    def pop(self):
        if self._top is None:
            raise StackError("Stack is empty")
        value = self._top.value
        self._top = self._top.next
        return value
    # 查看栈顶元素
    def top(self):
        if self._top is None:
            raise StackError("Stack is empty")
        return self._top.value
if __name__ == "__main__":
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
