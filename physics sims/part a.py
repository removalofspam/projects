# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:54:58 2020

@author: Will Davis
"""

" Creating Python Code for Part A of Project"
import math
import matplotlib as plot
import numpy as np


"Setting Variables"


#Setting variables of brewster angle calculation

#Index of refraction
n1 = 1   
n2 = 1.5
pi =3.14
n_t = n1/n2 

u1 = u2 = 1
a = 1
a

#DONOT NEED ALHPA HERE
#alpha
#def alpha(a):
#    for a in range(0, 90):
 #    ans =  ((1-((n_t) * (math.sin(a* (pi/180)))**2))/(math.cos(a)))
 #    print (ans)
      
#alpha(1)# CHECK TO SEE THAT THE NUMBERS ARE CORRECT

#beta
beta = ((u1 *n2)/(u2*n1))


#transmitted light  IT WORKS OMG
def transmitted(a):
    for a in range(0,91):
        alpha = math.sqrt(1 - ((n_t)*math.sin(a*(pi/180)))**2)/math.cos(a*(pi/180))
        
        
        transmit = ((alpha - beta)/(alpha + beta))**2
       
        
        print (str(a) + " = " +  str(transmit))


transmitted(1)
    
#reflected light
def reflected(a):
    for a in range(0,91):
        alpha = math.sqrt(1 - ((n_t)*math.sin(a*(pi/180)))**2)/math.cos(a*(pi/180))
        
        reflect = (alpha * beta) * ((2/(alpha +beta))**2)
        
        print (str(a) + " = " +  str(reflect))

reflected(1)

#plot setup USING MATLABPLOT will is a boss
time        = np.arange(0,90,10);

    