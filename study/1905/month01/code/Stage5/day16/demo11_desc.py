"""
demo11_desc.py  特征值矩阵
"""
import cv2 as cv
import matplotlib.pyplot as mp

original = cv.imread('../ml_data/table.jpg')
gray = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
# 特征点检测
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
# 提取特征值矩阵
_,desc = sift.compute(gray,keypoints)
print(desc.shape)
mp.imshow(desc.T,cmap='gist_rainbow')
mp.show()