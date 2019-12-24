"""
demo04_subplot.py 子窗口
"""
import matplotlib.pyplot as mp

for i in range(1,10):
    mp.figure('Subplot', facecolor='lightgray')
    mp.subplot(3,3,i)
    mp.text(0.5, 0.5, i, ha='center', va='center', size=36, alpha=0.6)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()
mp.show()