"""
Created on Tue Apr  7 01:54:58 2020

@author: Will Davis
"""

" Creating Python Code for Part A of Project"
import math
import matplotlib.pyplot as plot
import numpy as np


"Setting Variables"


#Setting variables of brewster angle calculation

#Index of refraction
#CHANGE THESE TO EDIT GRAPH
n1 = 1 
n2 = 1.5

pi =3.14
n_t = n1/n2 

u1 = u2 = 1
a = 1

#arrays for plot later -- 
rt_array = []
tr_array = []
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
        
        transmit = ((alpha - beta)/(alpha + beta))**2#quik maths - will
       #adding value to an array to plot
        tr_array.append(transmit)
        print (str(a) + " = " +  str(transmit))
        


transmitted(1)
    
#reflected light
def reflected(a):
    for a in range(0,91):
        alpha = math.sqrt(1 - ((n_t)*math.sin(a*(pi/180)))**2)/math.cos(a*(pi/180))
        
        reflect = (alpha * beta) * ((2/(alpha +beta))**2)
        
        #adding value to an array to plot
        
        rt_array.append(reflect)
        
        print (str(a) + " = " +  str(reflect))

reflected(1)

#plot setup USING MATLABPLOT  will is a boss


#RT ARRAY WORKS, TR ARRAY DOES NOT
# TR ARRRAY WORKS WOOOHOOOOO
plot.plot(tr_array,label='Transmitted')
plot.plot(rt_array,label='Reflected')
plot.legend()
plot.xlabel('Angle')
plot.ylabel
plot.grid(True) 
plot.show()  