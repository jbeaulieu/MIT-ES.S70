##################################
# Pset2 Question 2               #
# Filename: jbeaulieu_pset2_2.py #
##################################

from __future__ import division
from visual import *

from math import pi, sqrt
from const import E0
k = 1.0 / (4.0*pi*E0)

q=4*pi*E0
a=0.5

top=sphere(pos=(0,a,0), radius=0.2,color=color.red)  
bottom=sphere(pos=(0,-a,0), radius=0.2,color=color.blue)  

topCharge=[0,a,0,q]
bottomCharge=[0,-a,0,-q]

def EField(charge, location):
    r = (location[0] - charge[0], location[1] - charge[1], location[2] - charge[2])
    field = [k * (r[0] / sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))) * (charge[3] / (sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))**2)),
    k * (r[1] / sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))) * (charge[3] / (sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))**2)),
    k * (r[2] / sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))) * (charge[3] / (sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))**2))]
    return field
 
#at the origin
Etop=EField(topCharge,[0,0,0])
Ebottom=EField(bottomCharge,[0,0,0])
E=vector(Etop[0]+Ebottom[0],Etop[1]+Ebottom[1],Etop[2]+Ebottom[2])
arrow(pos=vector(0,0,0),axis=(.25 * E))
print "At the Origin: ", E

#Calculate the E-Field at a distance of 'a' (perpendicular to the dipole)
Etop=EField(topCharge,[a,0,0])
Ebottom=EField(bottomCharge,[a,0,0])
E=vector(Etop[0]+Ebottom[0],Etop[1]+Ebottom[1],Etop[2]+Ebottom[2])
arrow(pos=vector(a,0,0),axis=(.25 * E),color=color.yellow)
arrow(pos=vector(-a,0,0),axis=(.25 * E),color=color.yellow)
arrow(pos=vector(0,0,a),axis=(.25 * E),color=color.yellow)
arrow(pos=vector(0,0,-a),axis=(.25 * E),color=color.yellow)
print" At all points distance 'a': ", E
