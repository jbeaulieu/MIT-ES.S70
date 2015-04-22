#################################
# Title: Pset 6                 #
# Filename: jbeaulieu_pset5.py	#
# Original Author: Jon Beaulieu	#
# Most Recent Edit: 3/23/2015	#
#################################

from math import log

from math import pi
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__(self, capacitance, ref):
        self.capacitance = float(capacitance)
        self.q = 0.0

    def charge(self, voltage):
        self.q = self.capacitance * voltage
        self.ref[self] = self.q

class sphere_cylinder_cap(capacitor):
    def __init__(self, ref, rc, rs, h, s, qc, qs):
        self.ref = ref
        self.capacitance = E0 * area / sep
        self.q = 0.0
        self.rc=rc
        self.rs=rs
        self.h=h
        self.s=s
        self.qc=qc
        self.qs=qs
# The idea was either that you put together an integral of Gauss' Law
# from the sphere to the cylinder by computation, or that you perform
# the integral analytically and incorporate the answer into the script.

class superCap:
    def __init__(self, cap1, cap2, parallel):
        self.cap1=cap1
        self.cap2=cap2
        self.parallel=parallel

    def totalCap():
        if self.parallel == True:
            self.totalCap = self.cap1 + self.cap2
        else:
            self.totalCap = 1/((1/self.cap1) + (1/self.cap2))
        
