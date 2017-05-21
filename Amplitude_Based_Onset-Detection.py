import essentia
import essentia.standard
import essentia.streaming
from essentia.standard import *
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as pyp

#instantiating the audio loader:
loader = essentia.standard.MonoLoader(filename='open_001.wav')

#loading audio file into an arrat
audio = loader()

#Squaring the audio signal

audio_2 = audio * audio 

#Finding the array length of the audo file
n = len(audio)

#Defining time range array used for plotting
time_array = np.linspace(0,30,n)

#plotting audio signal and its square 
pyp.figure(1)
pyp.plot(time_array,audio)

pyp.figure(2)
pyp.plot(time_array,audio_2)

#pyp.show()

#Finding the Envelope of the squared signal
#Declaring the envelope function
env = Envelope()

as_envelope = env(audio_2)

#Plotting the envelope
pyp.figure(3)
pyp.plot(time_array,as_envelope)

#pyp.show()

#Finding the Discrete Derivative of the envelope Function
Fs = 44100.0
#dt = 1/Fs;
envelope_dd = np.diff(as_envelope)*Fs

i = 0
for i in range (n-1):
	if(envelope_dd[i] < 7):
		envelope_dd[i] = 0

#envelope_dd.append(0)
#Plotting the Discrete Derivative
pyp.figure(4)
time_array_1 = np.linspace(0,30,n-1)
pyp.plot(time_array_1,envelope_dd)

#pyp.show()

#Saving the array as a .wav file
#write("Beats.wav",44100,envelope_dd)