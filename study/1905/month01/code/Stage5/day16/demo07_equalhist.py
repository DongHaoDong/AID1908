"""
demo07_equalhist.py     直方图均衡化提高图片亮度
"""
import cv2 as cv
original = cv.imread('../ml_data/sunrise.jpg')
cv.imshow('sunrise',original)
cv.waitKey()
# 灰度图
gray = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
gray_ = cv.equalizeHist(gray)
cv.imshow('gray_',gray_)
# YUV：亮度，色度，饱和度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[:,:, 0] = cv.equalizeHist(yuv[:,:, 0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equalized Color', equalized_color)
cv.waitKey()
