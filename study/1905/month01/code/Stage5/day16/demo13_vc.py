"""
demo13_vc.py    视频捕获设备
"""
import cv2 as cv

# 获取视频捕捉设备
video_capture = cv.VideoCapture(0)
# 读取一帧
while True:
    frame = video_capture.read()[1]
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
# 释放视频捕捉设备
video_capture.release()
# 销毁cv的所有窗口
cv.destroyAllWindows()