"""
demo03_fft.py   傅里叶变换
"""
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(0,np.pi*4,1000)
y1 = 4*np.pi*np.sin(x)
y2 = 4/3*np.pi*np.sin(3*x)
y3 = 4/5*np.pi*np.sin(5*x)
# 叠加1000条线
n = 1000
y = np.zeros(n)
for i in range(1, n+1):
    y+=4/(2*i-1)*np.pi*np.sin((2*i-1)*x)
mp.subplot(121)
mp.grid(linestyle=':')
mp.plot(x,y1,label='y1',alpha=0.2)
mp.plot(x,y2,label='y2',alpha=0.2)
mp.plot(x,y3,label='y3',alpha=0.2)
mp.plot(x,y,label='y')
# 针对合成的方波傅里叶变换
import numpy.fft as nf
complex_ary = nf.fft(y)
y_ = nf.ifft(complex_ary).real   # 合成波
print(y_.dtype)
mp.plot(x,y_,label='y_',color='red',linewidth=7,alpha=0.2)
mp.tight_layout()
# 绘制频域图像    频率/能量图像
# 通过采样数量与采样周期获取fft的频率数组
freqs = nf.fftfreq(y_.size,x[1]-x[0])
pows = np.abs(complex_ary)  # 复数的模->能量
mp.subplot(122)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>0],pows[freqs>0],color='orangered',label='Freqency')
mp.legend()
mp.tight_layout()
mp.legend()
mp.show()