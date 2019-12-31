"""
demo09_reviews.py   电影评论情感分析
"""
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
import numpy as np
pdata = []
fileids = nc.movie_reviews.fileids('pos')
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    pdata.append((sample,'POSITIVE'))
ndata = []
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    ndata.append((sample,'NEGTIVE'))
# 整理数据集，80%训练，20%测试
pnumb,nnumb = int(len(pdata)*0.8),int(len(ndata)*0.8)
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model,test_data)
print(ac)
# 模拟业务场景
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']
sents, probs = [], []
for review in reviews:
    sample = {}
    words = review.split()
    for word in words:
        sample[word] = True
    pcls = model.classify(sample)
    print(review, '->', pcls)