"""
demo09_star.py  特征点检测
"""
import cv2 as cv
original = cv.imread('../ml_data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
print(len(keypoints),type(keypoints[0]))
mixture = original.copy()
cv.drawKeypoints(
    original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()