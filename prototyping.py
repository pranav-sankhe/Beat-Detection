#Prototyping to compute the Short Time Fourier Transform of the give audio snippet, and attempt to plot it
#Splitting the audio into k windows('hann'), and apply FFT(Spectrum) to each window. Choosing k optimally is our goal
#First attempt with k = 300
from essentia.standard import *
import numpy as np
import matplotlib.pyplot as pyp
import math 

#instantiating the audio loader:
loader = essentia.standard.MonoLoader(filename='open_001.wav')

#loading audio file into an array
audio = loader()

#Duration of the song
duration = Duration()
d = duration(audio)

#Numer of samples of the audio file
n = len(audio)

#Samling Rate
Fs = 44100 #Hz

#Number of samples
k = 300

#Duration of each window 
dur = d/k

#Samples in each Window
s = int(Fs * dur) 

#Defining the fft (spectrum magnitude)
spec = Spectrum()

#Windowing Function
w = Windowing(type = 'square')

#Defining the two dimensional array to store the fft values corresponding to each window
STFT = np.zeros((s/2+1,k))


i = 0
for i in range(k):
	frame = audio[int(i*dur*Fs) : int((i+1)*dur*Fs)]
	STFT[:,i] = spec(w(frame))

#Logarithmic Compression
#Compression Constant C
c = 2000

i = 0
j = 0
STFT_log_comp = np.zeros((s/2+1,k))

for i in range(k):
	for j in range(s/2+1):
		STFT_log_comp[j,i] = math.log((1+(c*STFT[j,i])),10)

#Defining the Time Array as the reference(to obtain dt as well)
time_array = np.linspace(0,d,k)
dt = d/k

#Computing the Discrete Derivative (As per the time in the 2-D array)
i = 0
j = 0
pre_novelty_curve = np.zeros((s/2+1,k-1))
for i in range(k-1):
	for j in range(s/2+1):
		if((STFT_log_comp[j,i+1]-STFT_log_comp[j,i]) > 0):
			pre_novelty_curve[j,i] = (STFT_log_comp[j,i+1]-STFT_log_comp[j,i])/dt
		else:
			pre_novelty_curve[j,i] = 0

#Summing up all the columns in the pre_novelty_curve
novelty_curve = np.zeros(k)
i = 0
j = 0
tsum = 0

for i in range(k-1):
	for j in range(s/2 + 1):
		tsum = tsum + pre_novelty_curve[j,i]
		novelty_curve[i] = tsum
	tsum = 0

#Plotting the normalized Novelty Curve(Involving Subtraction of Local(Moving) Average)
maxterm = max(novelty_curve)
novelty_curve = novelty_curve / maxterm
mav = MovingAverage()
mov_avg = mav(essentia.array(novelty_curve))

#Subtracting the moving average from the actual novelty_curve
i = 0
#Defining the difference curve as diff
diff = np.zeros(k)
for i in range(k):       
    if(novelty_curve[i]-mov_avg[i]>0):
        diff[i] = novelty_curve[i]-mov_avg[i]
    else:
        diff[i] = 0
pyp.figure(1)
pyp.plot(time_array,novelty_curve)
pyp.figure(2)
pyp.plot(time_array,mov_avg)
pyp.figure(3)
pyp.plot(time_array,diff)

#pyp.show()

#Peak Picking
#i = 0
#for i in range(k-1):
#	if(novelty_curve[i] < 0):
#		novelty_curve[i] = 0

#pyp.plot(time_array,novelty_curve)
#pyp.show()












