"""
demo12_objects    物体识别
"""
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import sklearn.svm as svm
import sklearn.metrics as sm
import os
import cv2 as cv

def search_files(directory):
    """
    检索directory目录下的所有文件，返回目录字典
    {'apple':[url,url,url,...],
     'banana':[url,url,url,...],
     'kiwi':[url,url,url,...],...}
    """
    objects = {}
    for curdir,subdirs,files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                url = os.path.join(curdir,file)
                objects[label].append(url)
    return objects
# 读取所有的训练样本
train_urls = search_files('../ml_data/objects/training')
# 整理训练集的输入与输出,训练svm模型
train_x,train_y = [],[]
for label,urls in train_urls.items():
    for file in urls:
        # 提取file图片特征值矩阵，整理样本
        image = cv.imread(file)
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        h,w = gray.shape
        # 计算伸缩比例，较小的边==200，较大的边自适应
        f = 200/min(h,w)
        gray = cv.resize(gray,None,fx=f,fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        # desc:(n,128)
        _,desc = sift.compute(gray,keypoints)
        sample = np.mean(desc,axis=0)
        train_x.append(sample)
        train_y.append(label)
train_x = np.array(train_x)
import sklearn.preprocessing as sp
encoder = sp.LabelEncoder()
train_y_labeled = encoder.fit_transform(train_y)
# 训练svm
model = svm.SVC(kernel='poly',degree=2,probability=True)
import sklearn.linear_model as lm
model = lm.LogisticRegression()
model.fit(train_x,train_y_labeled)
pred_train_y = model.predict(train_x)
print(sm.classification_report(train_y_labeled,pred_train_y))

# 读取所有的测试样本
test_urls = search_files('../ml_data/objects/testing')
# 整理训练集的输入与输出,训练svm模型
test_x,test_y = [],[]
for label,urls in test_urls.items():
    for file in urls:
        # 提取file图片特征值矩阵，整理样本
        image = cv.imread(file)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        h, w = gray.shape
        # 计算伸缩比例，较小的边==200，较大的边自适应
        f = 200 / min(h, w)
        gray = cv.resize(gray, None, fx=f, fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        # desc:(n,128)
        _, desc = sift.compute(gray, keypoints)
        sample = np.mean(desc, axis=0)
        test_x.append(sample)
        test_y.append(label)
test_x = np.array(test_x)
import sklearn.preprocessing as sp
test_y_labeled = encoder.transform(test_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y_labeled,pred_test_y))
# # 置信概率
probs = model.predict_proba(test_x)
print(np.round(probs,2))
for label,prob in zip(encoder.inverse_transform(pred_test_y),probs.max(axis=1)):
    print(label,prob)