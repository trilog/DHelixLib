#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dataX = list()
dataY = list()
dataZ = list()

with open("input.tsv", "r", newline = '') as inFile:
    csvreader = csv.reader(inFile, delimiter = '\t')
    for row in csvreader:
        dataX.append(float(row[0]))
        dataY.append(float(row[1]))
        dataZ.append(float(row[2]))

#fig = plt.figure(figsize=plt.figaspect(0.5))
fig = plt.figure()

ax = fig.add_subplot(121, projection='3d')
ax.set_aspect(1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.scatter(dataX, dataY, dataZ)

#a2 = fig.add_subplot(122, projection="3d")
#a2.set_aspect(1)
#a2.set_xlabel('X')
#a2.set_ylabel('Y')
#a2.set_zlabel('Z')
#a2.set_xlim(-10, 10)
#a2.set_ylim(-10, 10)
#a2.set_zlim(-10, 10)
#a2.plot(dataX, dataY, dataZ)

plt.show()
