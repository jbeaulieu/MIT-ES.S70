#####################################
# Title: VPython Video #1 Challenge #
# Filename: challenge1.py           #
# Original Author: Jon Beaulieu     #
# Most Recent Edit: 2/8/2015        #
# Last Editor: Jon Beaulieu         #
#####################################

from visual import *

# Left sphere/arrow
sphere(pos = vector(-1,0,0), radius = 0.5, color = color.green)
arrow(pos = vector(-1,0,0), axis=vector(0,-1,0), color = color.red)

# Upper right sphere/arrow
sphere(pos = vector(1,1,0), radius = 0.5, color = color.green)
arrow(pos = vector(1,1,0), axis=vector(-1,0,0), color = color.red)

# Lower left sphere/arrow
sphere(pos = vector(1,-1,0), radius = 0.5, color = color.green)
arrow(pos = vector(1,-1,0), axis=vector(1,1,0), color = color.red)
