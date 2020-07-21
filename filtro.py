# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:49:20 2020

@author: ng8569f
"""

#import numpy as np
from scipy.signal import butter,filtfilt
import csv
import  matplotlib.pyplot as plt

signal_R = []
with open('fuerza_sin_filtrar1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', )
    for elem in spamreader:
        signal_R.append(float(str(elem[0])))
        
        
        
        
signal_L = []
with open('fuerza_sin_filtrar1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', )
    for elem in spamreader:
        signal_L.append(float(str(elem[0])))
        
        
        
        
        
        
# Filter requirements.
T = 0.0100         # Sample Period
fs = 128       # sample rate, Hz
cutoff = 5      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
nyq = 0.5 * fs  # Nyquist Frequency
order = 2       # sin wave can be approx represented as quadratic
n = int(T * fs) # total number of samples

def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y




data =signal_L
# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)
x = list(range(0,len(y)))

fig = plt.figure()
plt.plot(x, signal_L, color='black',alpha=0.5)
plt.plot(x, y, color='tab:blue')
