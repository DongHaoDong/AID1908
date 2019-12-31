"""
demo02_mfcc.py    mfcc矩阵
"""
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp

sample_rate,sigs = wf.read('../ml_data/speeches/freq.wav')
print(sample_rate,sigs.shape)
mfcc = sf.mfcc(sigs,sample_rate)
mp.imshow(mfcc.T,cmap='gist_rainbow')
mp.tight_layout()
mp.show()