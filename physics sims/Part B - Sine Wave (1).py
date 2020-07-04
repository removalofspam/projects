# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:33:00 2020

@author: Will Davis
"""

import numpy as np

import matplotlib.pyplot as plot

 
#setting Variables

pi =3.14

c = 299792458  # speed of light?



#INPUT LAMDA/WAVELENGTH VALUE
la = 0.00000050      #
phi = 0
# and phase diff

t = 0 # should be a standing wave?

f = c/la

w = (2 * pi * f)

k = (2 * pi)/la
# Get x values of the sine wave 
#E = 1
#therefore sine values of time i.e. sin(kz-wt) will give value of E at given time
time        = np.arange(0, 5, 0.1);

 
z = time
# Amplitude of the sine wave is sine of a variable like time

amplitude   = np.sin(k * time - (w * t))

 

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, amplitude)

 

# Give a title for the Plane wave plot

plot.title('Plane wave Propagation')

 

# Give x axis label for the sine wave plot

plot.xlabel('Time')

frequency = "Frequency =" + str(f)

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.text(0.05, 0.95, frequency, fontsize=10,bbox=dict(facecolor='white', alpha=0.5))
 

plot.grid(True, which='both')

 

plot.axhline(y=0, color='k')

 

plot.show()

wavelength = la * 10000

print("Wavelength = " + str(la))
print("Frequency = " + str(f/1000) + " kHz ")

# Display the sine wave

plot.show()



plot.plot([0, 1, 2, 3])