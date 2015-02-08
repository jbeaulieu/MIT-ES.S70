#####################################
# Title: VPython Video #2 Challenge #
# Filename: challenge2.py           #
# Original Author: Jon Beaulieu     #
# Most Recent Edit: 2/8/2015        #
# Last Editor: Jon Beaulieu         #
#####################################

from visual import *

#Sphere declarations
leftSphere = sphere(pos = vector(-1,0,0), radius = 0.25, color = color.green)
topRightSphere = sphere(pos = vector(1,1,0), radius = 0.25, color = color.green)
bottomRightSphere = sphere(pos = vector(1,-1,0), radius = 0.25, color = color.green)

#Connecting arrows
arrow(pos = topRightSphere.pos, axis = leftSphere.pos - topRightSphere.pos, color = color.red)
arrow(pos = leftSphere.pos, axis = bottomRightSphere.pos - leftSphere.pos, color = color.red)
arrow(pos = bottomRightSphere.pos, axis = topRightSphere.pos - bottomRightSphere.pos, color = color.red)
