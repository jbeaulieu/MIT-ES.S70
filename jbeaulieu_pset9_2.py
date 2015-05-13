#################################
# Pset 9, part 2                #
# Filename: jbeaulieu_pset9_2.py#
# Original Author: Jon Beaulieu #
# Most Recent Edit: 5/10/2015   #
#################################

from __future__ import division
from visual import *
import numpy
from math import pi

charge = sphere(pos=(2,2,2), radius=0.2)

positionRecord = []

fileName = 'jbeaulieu_pset9_output.txt'

with open(fileName, 'r', 0) as filePath:
    rawLine = filePath.readline()
    
    while rawLine:

        lineData = []
        data = []
        #position = numpy.array((0,0,0))

        lineData = rawLine.split(', ')
        for i in lineData:
            data.append(i.strip('])([\n'))

        charge.pos = (data[0], data[1], data[2])

        rawLine = path.readline()
