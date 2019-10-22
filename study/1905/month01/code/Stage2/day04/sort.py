"""
sort.py 排序算法训练
"""
# 冒泡排序
def bubble(list_):
    # 外层表示比较多少轮
    for i in range(len(list_)-1):
        # 内从循环表示每轮两两比较的次数
        for j in range(len(list_)-1-i):
            # 从大到小排序
            if list_[j] < list_[j+1]:
                list_[j],list_[j+1] = list_[j+1],list_[j]
# 完成一轮排序
def sub_sort(list_,low,high):
    # 选定基准
    x = list_[low]
    # low向后，high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = x
    return low

# 快速排序
def quick(list_,low,high):
    # low表示列表第一个元素索引，high表示最后一个元素索引
    if low < high:
        key = sub_sort(list_,low,high)
        quick(list_,low,key-1)
        quick(list_,key+1,high)

# 选择排序
def select(list_):
    # 每轮选择最小值，需要len(list_)-1轮
    for i in range(len(list_)-1):
        min = i     # 假设list_[i]为最小值
        for j in range(i+1,len(list_)):
            if list_[min] > list_[j]:
                min = j     # 擂主换人
        # 进行交换，将最小值换到了应该在的位置
        if min != i:
            list_[i],list_[min] = list_[min],list_[i]

# 插入排序
def insert(list_):
    # 判断每次比较的数是谁，从第二个数开始
    for i in range(1,len(list_)):
        x = list_[i]    # 空出list_[i]的位置
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1]=x

l = [4,9,3,1,5,2,8,4]
# bubble(l)
# quick(l,0,len(l)-1)
# select(l)
insert(l)
print(l)
