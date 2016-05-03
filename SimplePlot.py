#!/usr/bin/python

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs = list()
ys = list()
zs = list()

with open("input.tsv", "r", newline = '') as inFile:
    csvreader = csv.reader(inFile, delimiter = '\t')
    for row in csvreader:
        xs.append(float(row[0]))
        ys.append(float(row[1]))
        zs.append(float(row[2]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.scatter(xs, ys, zs)

plt.show()
