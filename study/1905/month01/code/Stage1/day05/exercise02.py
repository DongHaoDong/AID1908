"""
    在控制台中录入学生成绩,输入空字符串,打印所有成绩
    打印最高分,最低分,平均分
"""
scores = []
# 录入过程
while True:
    score = input("请输入学生成绩:")
    if score == "":
        break
    scores.append(float(score))
# 输出过程
for item in scores:
    print(item)
# 计算最高分
max_score = max(scores)
# 计算最低分
min_score = min(scores)
# 计算平均分
avg_score = sum(scores) / (len(scores))
# 打印最高分,最低分,平均分
print("最高分是{},最低分是{},平均分是{}".format(max_score, min_score, avg_score))

