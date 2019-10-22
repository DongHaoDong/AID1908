from LinkList import *

l1 = LinkList()
l2 = LinkList()

l1.init_list([1,5,7,8,10,19])
l2.init_list([0,3,4,9])

l1.show()
l2.show()

def merge(list_target01,list_target02):
    # 将list_target02合并到list_target01中
    p = list_target01.head
    q = list_target02.head.next
    while p.next is not None:
        if p.next.value < q.value:
            p = p.next
        else:
            temp = p.next
            p.next = q
            p = p.next
            q = temp
    p.next = q
merge(l1,l2)
print("===============================")
l1.show()