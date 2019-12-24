"""
demo06_axes.py
"""
import matplotlib.pyplot as mp

mp.figure('Flow Layout',facecolor='lightgray')
# 设置图表位置，给出左下角点坐标宽与高即可
# left_bottom_x:左下角x坐标
# left_bottom_y:左下角y坐标
# width:        宽度
# height:       高度
# mp.axes([left_bottom_x,left_bottom_y,width,height])
mp.axes([0.03,0.5,0.94,0.4])
mp.text(0.5,0.5,'1',ha='center',va='center',size=36)

mp.axes([0.03,0.03,0.54,0.4])
mp.text(0.5,0.5,'1',ha='center',va='center',size=36)
mp.show()