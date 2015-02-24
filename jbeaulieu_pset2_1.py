##################################
# Title: Pset 2 Question 1       #
# Filename: jbeaulieu_pset2_1.py #
# Original Author: Jon Beaulieu	 #
# Most Recent Edit: 2/24/15	 #
##################################

from math import sqrt, pi
from const import E0
k = 1.0 / (4 * pi * E0)

print "Enter point charge data in form x,y,z,q"
chargeData = tuple(int(x.strip()) for x in raw_input().split(','))

#parse point charge data from user input
charge_x = chargeData[0]
charge_y = chargeData[1]
charge_z = chargeData[2]
charge_q = chargeData[3]

print "Enter location in form x,y,z"
location = tuple(int(x.strip()) for x in raw_input().split(','))

#parse location data from user input
location_x = location[0]
location_y = location[1]
location_z = location[2]

# Calculate the electric field individually in each dimension
E_x = (k * charge_q) / ((location_x - charge_x)**2)
E_y = (k * charge_q) / ((location_y - charge_y)**2)
E_z = (k * charge_q) / ((location_z - charge_z)**2)

# Get the total electric field by adding the previous three as a vector
E_total = [E_x, E_y, E_z]
print 'E =', E_total, 'N/C'
