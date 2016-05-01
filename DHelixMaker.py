#!/usr/bin/python

import csv
from math import pi, sin, cos

def Helix(r, c, t, theta, phi):
    return (r*cos(2*pi*t)*sin(theta)*cos(phi), r*sin(2*pi*t)*sin(theta)*sin(phi), c*t*cos(theta))

points = 40
ppc = 10
radius = 2
c = 4
theta = 0 * pi/180
phi = 90 * pi/180


with open("input.tsv", 'w', newline='') as outFile:
    csvwriter = csv.writer(outFile, delimiter='\t')
    for t in range(0, points):
        csvwriter.writerow(Helix(radius, c, t/ppc, theta, phi))
