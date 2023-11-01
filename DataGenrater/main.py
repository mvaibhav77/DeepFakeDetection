from scipy.io.wavfile import read, write
# from scipy.signal import resample, decimate
# # from librosa import resample
# import tensorflow_io as tfio
from matplotlib import pyplot as plt
from uuid import uuid4
# import audresample
import numpy as np

# FS, data = read("../source/videoplayback.wav")
# number_of_samples = round(len(data) * float(32000) / FS)
# data1 = tfio.audio.resample(data,FS,32000)
# print(data1[::,1].shape)
# # print(np.linspace(start=0,stop=11098112))
# plt.plot(np.arange(0,len(data)),data[::,1],color="b",alpha=0.2)
# # plt.show()
# plt.plot(np.arange(0,len(data1)),data1[::,1],color="r",alpha=0.3)
# plt.show()


# write("data.wav",32000,data1)

import librosa    
y, s = librosa.load('../source/videoplayback.wav', sr=32000)

print(len(y))
print(s)
plt.plot(np.arange(0,len(y)),y,color="r",alpha=0.3)
plt.show()
for i in range(1,41):
    write(f"{str(uuid4())}.wav",32000,y[(i-1)*32000*6:i*32000*6])