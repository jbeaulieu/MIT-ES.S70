##################################
# Pset 4 Question 4              #
# Filename: jbeaulieu_pset4_1.py #
# Original Author: Jon Beaulieu  #
##################################

from __future__ import division
from visual import *

from math import pi, sqrt
from const import E0
k = 1.0 / (4.0*pi*E0)
q = 1.0E-6
sigma = 1.0E-3
integral = 0.0
force = 0.0

print q, sigma

# Instead of integrating over the entire blanket, my script will integrate over
#  one quadrant of the blanket, then multiply the resulting flux by four

for y in range(1,1000):
    for x in range(1,1000):
        integral += (k*q)/((math.sqrt(1 + (x*.001)**2 + (y*.001)**2))**(3.0))

total = integral * 4
print total

# Calculating the vector force is similar to the above flux, but without the
#  Correction for only taking the perpendicular component. We then multiply the
#  E-field at each point by the charge density of the blanket to get the force

for y in range(1,1000):
    for x in range(1,1000):
        force += (k*q*sigma)/(1 + (x*.001)**2 + (y*.001)**2)

force *= 4
print force
