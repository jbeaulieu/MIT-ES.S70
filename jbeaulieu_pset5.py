#################################
# Title: Pset 5                 #
# Filename: jbeaulieu_pset5.py	#
# Author: Jon Beaulieu  	#
# Most Recent Edit: 3/23/2015	#
#################################

import time
import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp, cos, sin
from const import E0

k = 1.0 / (4 * pi * E0)

Volts=[]
rodLength=[]

for step in np.arange(0,0.5,0.01):
    rod = np.array([step*2, 0.25-step, step])
    v = 0
    
    for theta in np.arange(-pi/2,pi/2,pi/1000):
        x = (0.5 * cos(theta))
        y = 0
        z = (0.5 * sin(theta)) + 0.5
        q = (10^(-6))/(1 + exp(-5*(theta-pi/2)))
        r = sqrt(((rod[0] - x)**2) + ((rod[1] - y)**2) + ((rod[2] - z)**2))
        v += (k*q)/r
        
    rodLength.append(rod[0])
    Volts.append(v)

plot(rodLength, Volts)
show()
