# not completed
from math import sqrt, sin, cos, tan, pi
from math import asin, acos, atan

# C/2012 S1 (Comet ISON)
node = 295.65203155 # longitude of the ascending node (deg)
i = 62.40397752235779 # inclination

e = 1.000201003833968 # eccentricity
a = 61.95201446552018 # semi-major axis (AU)
q = 0.01245259242960607 # perihelion distance (AU)
peri = 345.5312406205832 # argument of perihelion (deg)

n = 0.002021254151162501 # mean daily motion (deg/d)
M = 0.01055365863920281 # mean anomaly
tp = 2456625.278658273561 # perihelion passage
period = None # period

# calc
b = 5 * (1-e) / (1+9*e)
B = 1 - 0.017142857 * A**2 - 0.003809524 * A**3

# recurence
M1 = a * (t - tp) / q ** 1.5
W1 = atan(tan(v/2))
