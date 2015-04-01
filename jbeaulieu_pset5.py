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
    rod = np.array([step*2, 0.25-step, step])# Isn't this `path`, not `rod`?
    v = 0# You used `rod` correctly for what it was, so no complaints.
    
    for theta in np.arange(-pi/2,pi/2,pi/1000):
        x = (0.5 * cos(theta))
        y = 0
        z = (0.5 * sin(theta)) + 0.5

	# This isn't q, it's lamda. You want dq = r * lamda * dtheta
        q = (10^(-6))/(1 + exp(-5*(theta-pi/2)))# Try: 1e-6 = 1 * 10^-6

        r = sqrt(((rod[0] - x)**2) + ((rod[1] - y)**2) + ((rod[2] - z)**2))
	# Try this: r = np.linalg.norm(rod - np.array((x, y, z)))

        v += (k*q)/r
	# And this would be k * dq / r
        
    rodLength.append(rod[0])
    Volts.append(v)# A list of the voltages at each point. Good.

plot(rodLength, Volts)# We just wanted the progress along path, but this provides more info
show()
