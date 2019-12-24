"""
demo05_grid.py
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid Layout', facecolor='lightgray')
gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2])    # 0行 前两列
mp.text(0.5,0.5,'1',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[:2,2])
mp.text(0.5,0.5,'2',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1,1])
mp.text(0.5,0.5,'3',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1:,0])
mp.text(0.5,0.5,'4',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[-1,1:])    # 0行 前两列
mp.text(0.5,0.5,'5',size=36,alpha=0.6,ha='center',va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()