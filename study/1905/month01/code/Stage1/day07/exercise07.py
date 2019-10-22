"""
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素两两比较,发现相同的打印结果
        所有元素比较结束,都没有发现相同项,则打印结果
"""
list01 = [3, 80, 45, 21, 25, 1]
# 结果:假设没有相同项
result = False
for row in range(len(list01)-1):
    for col in range(row+1, len(list01)):
        if list01[row] == list01[col]:
            print("具有相同项!")
            result = True
            break
    if result:
        break
if result == False:
    print("没有相同项！")