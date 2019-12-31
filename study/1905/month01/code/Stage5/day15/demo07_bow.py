"""
demo07_bow.py   词袋模型
"""
import numpy as np
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sents = tk.sent_tokenize(doc)
print(sents)
# 构建词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(sents)
print(bow.toarray())
print(cv.get_feature_names())
# 输出tfidf矩阵
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(np.round(tfidf.toarray(),2))