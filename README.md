# Beat-Detection
Beat Tracking and Tempo Estimation of Audio Signals

### Introduction to Beat Detection


This project aims to estimate beat positions in the given audio file. Some of the methods I am using are - 
- **Energy Changes Based Detection**: Observe any changes in the Energy Content in the signal, which is proportional to the Amplitude Squared of the signal. The procedure is as follows - 
	- Amplitude Squaring(Energy Proportionality)
	- Envelope Detection(Using Hilbert Transform or Moving Average Techniques)
	- Discrete Difference(Changes in Energy Content)
	- Rectification(Only considering Positive Differences(For Energy Increases, not decreases))
	- Peak Picking(Based on Threshold Values, which depend on the kind of audio)

**Note:** One Major issue with this method is that it is difficult to detect weak note offsets such as that of stringed instruments or others. It works best for strong energy changes in signals, for example percussion instruments.

- **Spectrum Changes Based Detection**: Computing the _Short-Time Fourier Transform_, and observing changes in the spectra. The procedure is as follows:
	- Computing the Short Time Fourier Transform ( Basically the FFT applied to a window of appropriate type and size )
	- Logarithmic Compression - Elaborate the more detailed changes in frequency
	- Discrete Difference(Same as above)
	- Accumulation - Add up all the differences in the array to signify all the changes in the spectrum content)
	- Normalization
	- Peak Picking(Same as above)

All the code for the above methods has been written in Python with the help of Essentia, a set of audio-manipulation tools available online. 
