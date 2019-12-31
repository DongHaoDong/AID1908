"""
demo06_canny.py     边缘识别
"""
import cv2 as cv
original = cv.imread('../ml_data/chair.jpg',cv.IMREAD_GRAYSCALE)
print(original)
cv.imshow('original',original)
# 索贝尔边缘识别
sobel = cv.Sobel(original,cv.CV_64F,0,1,ksize=5)
cv.imshow('sobel',sobel)
# 拉普斯边缘识别
laplacian = cv.Laplacian(original,cv.CV_64F)
cv.imshow('laplacian',laplacian)
# Canny边缘识别
canny = cv.Canny(original,50,200)
cv.imshow('canny',canny)
cv.waitKey()