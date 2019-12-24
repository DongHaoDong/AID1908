"""
demo07_locator.py 刻度定位器
"""
import matplotlib.pyplot as mp
locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator([3,6,9])',
            'mp.AutoLocator()']
mp.figure('locators',facecolor='lightgray')
# 整理坐标轴
for i,locator in enumerate(locators):
    mp.subplot(len(locators),1,i+1)
    mp.xlim(1,10)
    ax = mp.gca()
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data',0.5))
    mp.yticks([])
    loc = eval(locator)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.show()
