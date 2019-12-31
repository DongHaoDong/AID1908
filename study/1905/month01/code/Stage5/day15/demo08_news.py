"""
demo08_news.py  主题识别
"""
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import numpy as np

train = sd.load_files('../ml_data/20news',encoding='latin1',shuffle=True,random_state=7)
train_data = np.array(train.data)
train_y=np.array(train.target)
categories = np.array(train.target_names)
print(train_data.shape,train_y.shape,categories.shape)
print(train_data[0],train_y[0],categories)
# 构建tfidf模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(train_data)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
# 训练基于多项分布的朴素贝叶斯
model = nb.MultinomialNB()
model.fit(tfidf,train_y)
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two0wheeler is really good on slippery roads'
]
test_bow = cv.transform(test_data)
test_tfidf = tt.transform(test_bow)
pred_y = model.predict(test_tfidf)
print(categories[pred_y])