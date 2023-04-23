"""AOC Day 12 Solutions"""

#
# probably doesn't make sense to use a graph
#

import networkx as nx
import matplotlib.pyplot as plt

#inpt = open("input\\day12_input.txt", "r", encoding="utf-8").read().splitlines()
inpt = open("input\\day12_sample_input.txt", "r", encoding="utf-8").read().splitlines()

# Problem:
# Want to get from S (elevation a) to E (elevation z)
# Can go up 1 in height or down an unlimited amount
# Can only move to adjacent positions, not diagonal ones


# need to use directed graphs because you may be able to jump down but not back up
G = nx.digraph()
# generate graph from inpt here
for row in inpt:
    for pos in row:
# note location of S and change it to its elevation (0/a)
# note location of E and change it to its elevation (25/z)
    

nx.draw(G)
plt.show()
