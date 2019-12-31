"""
demo03_reco.py      电影推荐引擎
"""
import json
import numpy as np
with open('../ml_data/ratings.json','r') as f:
    ratings = json.loads(f.read())
users = list(ratings.keys())
scmat = []
for user1 in users:
    scrow = []
    for user2 in users:
        # 计算user1与user2的欧氏距离得分
        movies = set()  # 整理两人都看过的电影
        for movie in ratings[user1]:
            if movie in ratings[user2]:
                movies.add(movie)
        if len(movies) == 0:    # 两人没有共同语言
            score = 0
        else:
            A,B=[],[]   # 存储两个人对相同电影的打分
            for movie in movies:
                A.append(ratings[user1][movie])
                B.append(ratings[user2][movie])
            A,B=np.array(A),np.array(B)
            # score = 1/(1+np.sqrt(((A-B)**2).sum()))
            score = np.corrcoef(A,B)[0,1]
        scrow.append(score)
    scmat.append(scrow)
scmat = np.array(scmat)
print(np.round(scmat,2))
# 按照相似度从高到低排列每个用户的相似用户，实现召回算法
users = np.array(users)
scmat = np.array(scmat)
for i,user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i,sorted_indices]
    print(user,similar_users,similar_scores)
    # 找到所有正相关用户
    positive_mask = similar_scores > 0
    similar_users = similar_users[positive_mask]
    # 整理字典的数据结构，存储召回电影列表
    rec0_movies = {}
    for i,sim_user in enumerate(similar_users):
        for movie,score in ratings[sim_user].items():
            if movie not in ratings[user].keys():
                # 存入推荐字典
                if movie not in rec0_movies:
                    rec0_movies[movie]=[score]
                else:
                    rec0_movies[movie].append(score)
    # 排序算法
    movielist = sorted(rec0_movies.items(),key=lambda x:np.mean(x[1]),reverse=True)
    print(user)
    print(movielist)



