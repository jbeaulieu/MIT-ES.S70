#################################
# Pset 9, part 1                #
# Filename: jbeaulieu_pset9_1.py#
# Original Author: Jon Beaulieu #
# Most Recent Edit: 5/10/2015   #
#################################

from math import pi, sqrt, sin, cos, atan
import numpy
from const import mu0, E0

# Initial Conditions

m = 10e-22
q = 1.6e-19
lamda = 1e-15
I = 1e-4
dt = 1e-3

p_0 = numpy.array((2., 2., 2.))
v_0 = numpy.array((5., 5., 5.))

# This script will assume that the wire runs infintely along the x-axis,
#  meaning that the vector from the positive charge to the wire will have
#  a y-component and a z-component, but no x-component

with open('jbeaulieu_pset9_output.txt', 'w', 0) as text:

    for i in xrange(1000):
        r = numpy.array((0, p_0[1], p_0[2]))
        r_abs = sqrt(r[0]**2 + r[1]**2 + r[2]**2)
        theta = atan(p_0[2]/p_0[1])

        # Force derivation
        E_abs = lamda / (2*pi*E0*r_abs)
        F_e = numpy.array((0, q*E_abs*cos(theta), q*E_abs*sin(theta)))

        B_abs = (mu0 * I)/(2 * pi * r_abs)
        B = numpy.array((0, B_abs*cos(theta), B_abs*sin(theta)))
        F_b = numpy.cross(q*v_0, B)

        F = F_e + F_b

        # Update particle information
        a = numpy.array(F/m)
        v_0 += (a*dt)
        p_0 += (v_0*dt)
        
        text.write(str((p_0.tolist(), v_0.tolist(), a.tolist())) + '\n')
