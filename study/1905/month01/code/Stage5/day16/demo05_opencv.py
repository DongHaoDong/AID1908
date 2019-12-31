"""
demo05_opencv.py    图像识别
"""
import cv2 as cv
import numpy as np
original = cv.imread('../ml_data/forest.jpg')
cv.imshow('original',original)
# 切出图像的三通道数据
blue = np.zeros_like(original)
blue[:,:,0] = original[:,:,0]
cv.imshow('blue',blue)
green = np.zeros_like(original)
green[:,:,1] = original[:,:,1]
cv.imshow('green',green)
red = np.zeros_like(original)
red[:,:,2] = original[:,:,2]
cv.imshow('red',red)
# 图像裁剪
h,w = original.shape[:2]
t,b = int(h/4),int(h*3/4)
l,r = int(w/4),int(w*3/4)
cropped = original[t:b,l:r]
cv.imshow('cropped',cropped)
# 图像缩放
resize = cv.resize(original,(int(w/4),int(h/4)))
cv.imshow('resize',resize)
resize = cv.resize(resize,None,fx=4,fy=4)
cv.imshow('resize2',resize)
# 图像的保存
cv.imwrite('green.jpg',green)
cv.waitKey()