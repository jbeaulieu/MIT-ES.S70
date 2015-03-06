##################################
# Pset 4 Question 2              #
# Filename: jbeaulieu_pset4_2.py #
# Original Author: Jon Beaulieu  #
##################################

from __future__ import division
from visual import *

from math import pi, sqrt
from const import E0

charge = sphere(pos=(0,0,0), radius = 0.1, color = color.red)
blanket = box(pos=(0,0,1), axis=(0,0,1), length=.001, height=2, width=2, color = color.blue)

arrow(pos=(0.25,0.25,0), axis=(0.5,0.5,0.5), color = color.yellow)
arrow(pos=(0.25,-0.25,0), axis=(0.5,-0.5,0.5), color = color.yellow)
arrow(pos=(-0.25,0.25,0), axis=(-0.5,0.5,0.5), color = color.yellow)
arrow(pos=(-0.25,-0.25,0), axis=(-0.5,-0.5,0.5), color = color.yellow)
