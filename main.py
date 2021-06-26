#!/usr/bin/env python3

import case
import solver
import re
import os
import time
import shelve
import matplotlib as m

# XXX USER Interaction variable

# Force
force = 0
# High
high = 0
# Initial High
initialHigh = 0
# Displacement
displacement = 0
# Initial Displacement
initialDisplacement = 0
# Speed
speed = 0
# Initial Speed
initialSpeed = 0
# Acceleration
acceleration = 0
# Constant Acceleration
constantAcceleration = 0
# Time
time = 0
# Initial Time
initialTime = 0


# XXX UNIVERSAl CONSTANT

# Gravity acceleration
GRAVITY = 9.81


# XXX Units > SI

# meter     (m)
# second    (s)
# Newton    (N)


# provide a case 

print(case.case_i())
