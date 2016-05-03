#!/usr/bin/python

import numpy as np
from math import pi, sin, cos

def Helix(r, c, t):
    return np.matrix((r*cos(2*pi*t), r*sin(2*pi*t), c*t)).T

def Rotation(origin, point, thetaX, thetaY, thetaZ):
    RX = np.matrix([[1, 0, 0], [0, cos(thetaX), -sin(thetaX)], [0, sin(thetaX), cos(thetaX)]])
    RY = np.matrix([[cos(thetaY), 0, sin(thetaY)], [0, 1, 0], [-sin(thetaY), 0, cos(thetaY)]])
    RZ = np.matrix([[cos(thetaZ), -sin(thetaZ), 0], [sin(thetaZ), cos(thetaY), 0], [0, 0, 1]])
    RTot = RX * RY * RZ
    return RTot * (point - origin)


    

points = 40
ppc = 10
radius = 2
c = 4
thetaX = 15 * pi/180
thetaY = 90 * pi/180
thetaZ = 0 * pi/180
origin = np.matrix([0, 0, 0]).T

import csv
with open("input.tsv", 'w', newline='') as outFile:
    csvwriter = csv.writer(outFile, delimiter='\t')
    for t in range(0, points):
        point = Helix(radius, c, t/ppc)
        rotatedPoint = Rotation(origin, point, thetaX, thetaY, thetaZ)
        newPoint = flatten(rotatedPoint.flat.copy().tolist()))
        print(newPoint)
        csvwriter.writerow(newPoint)
