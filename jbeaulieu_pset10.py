#################################
# Pset 10                       #
# Filename: jbeaulieu_pset10.py #
# Original Author: Jon Beaulieu #
# Most Recent Edit: 5/10/2015   #
#################################

import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy
import math
from const import mu0

# NOTE regarding coordinate system:
#  This script assumes the ring lies in the xy-plane, centered around the origin
#  (so that z=0 for any point along the ring)

a = input("Enter radius of each ring: ")
I = input("Enter current through the system: ")

def B_ring(point):

    total_B = numpy.array((0.0, 0.0, 0.0))
    steps = int(2*math.pi/0.001)
    
    for i in xrange(steps):
        angle = i*0.001
        r = point - numpy.array((math.cos(angle), math.sin(angle), 0))
        r_abs = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)

        # Use Biot-Savart to calculate B at given point
        dl = 0.001 * a * numpy.array((-1*math.sin(angle), math.cos(angle), 0.0))
        db = mu0 * I * numpy.cross(dl, r) / (4.0 * math.pi * r_abs**3)

        # Increment B accordingly
        total_B += db

    return total_B

# NOTE regarding coordinate system:
#  This script assumes the solenoid rings are parallel to the xy-plane
#  (like the ring in the script above). It further assumes the solenoid has
#  one end resting on the xy-plane, centered around the origin, and extends in
#  positive z direction toward its other end.

def B_solenoid(point):
    N = input("Enter number of loops: ")
    L = input("Enter length of solenoid: ")

    ring_separation = (1.0*L)/(N-1) #distance between each 'ring'
    final_B = numpy.array((0.0, 0.0, 0.0))

    for i in range(N):
        # Adding i*ring_separation adjusts for each succesive ring being
        #  further up the z-axis
        temp = B_ring(point + i*numpy.array((0,0,ring_separation)))
        final_B += temp
    
    return final_B
