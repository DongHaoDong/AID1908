"""
demo04_filter.py     频域滤波降噪
"""
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

# 采样率   采样位移
sample_rate,noised_sigs = wf.read('../da_data/noised.wav')
noised_sigs = noised_sigs/(2**15)
print(sample_rate,noised_sigs.shape)
# 绘制音频时域的:时间/位移图像
times = np.arange(noised_sigs.size) / sample_rate
mp.figure('Filter',facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain',fontsize=16)
mp.ylabel('Noised Signal',fontsize=12)
mp.grid(linestyle=":")
mp.plot(times[:178],noised_sigs[:178],color='dodgerblue',label='Noised')
mp.legend()
mp.tight_layout()
# 基于傅里叶变换，获取音频频域信息，
freqs = nf.fftfreq(times.size,times[1]-times[0])
complex_ary = nf.fft(noised_sigs)
pows = np.abs(complex_ary)
# 绘制音频频域的：频率/能量图像。
mp.subplot(222)
mp.title('Frequency Domain',fontsize=16)
mp.ylabel('power',fontsize=12)
mp.grid(linestyle=":")
mp.semilogy(freqs[freqs>0],pows[freqs>0],color='orangered',label='Noised')
mp.legend()
mp.tight_layout()
# 将低频噪声去除后绘制音频频域的：频率/能量图像
# 找到能量最大的正弦函数的频率
fund_freq = freqs[pows.argmax()]
noised_inds = np.where(freqs != fund_freq)
# 把噪声位置的复数数据抹掉
complex_ary[noised_inds] = 0
pows = np.abs(complex_ary)
mp.subplot(224)
mp.ylabel('power',fontsize=12)
mp.grid(linestyle=":")
mp.plot(freqs[freqs>0],pows[freqs>0],color='orangered',label='Filter')
mp.legend()
mp.tight_layout()
# 针对滤波后的复数数组，做逆向傅里叶变换
# 绘制时域图像：时间/位移图像
filter_sigs = nf.ifft(complex_ary)
mp.subplot(223)
mp.ylabel('Filter Signal',fontsize=12)
mp.grid(linestyle=":")
mp.plot(times[:178],filter_sigs[:178],color='dodgerblue',label='Filter')
mp.legend()
mp.tight_layout()
# 输出音频文件
wf.write('../da_data/filter.wav',sample_rate,(filter_sigs*2**15).astype(np.int16))
mp.show()