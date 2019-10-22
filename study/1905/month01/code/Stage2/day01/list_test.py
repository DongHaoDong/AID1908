from LinkList import *
import time
l = [i for i in range(999999)]
link = LinkList()
link.init_list(l)
tm = time.time()
# for i in L:
#     print(i)  # 列表
# link.show()     # 链表
# l.append(8866)
# link.append(8866)   # 尾插入
# l.insert(0,8866)
# link.head_insert(8866)  # 头插入
# link.insert(100,9999)
# link.delete(1)  # 删除
l.remove(1)
# link.show()
# print(link.get_index(7))
print("time:",time.time()-tm)
