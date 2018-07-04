#! /usr/bin/python2.7

import csv
from collections import defaultdict
import pandas as pd

filename = 'chordData.csv'
# Read the CSV into a pandas data frame (df)
df = pd.read_csv(filename, delimiter=',')
# Convert df to tuples
chordHistory = [tuple(x) for x in df.values]

d = defaultdict(list)
for line in chordHistory:
    print line
    print "\n"
    d[line[0]].append(line[1:])

print(d)

#myDict = defaultdict(list)
#
# def sortDictKeys(dict):
#     #returns new dict with keys (tuples) sorted
#     newDict = {}
#     for key in dict:
#         sortedKey = tuple(sorted(key))
#         newDict[sortedKey] = dict[key]
#     return newDict
#
# def sortChords(a,b):
#     #returns tuple of sorted chords
#     return tuple(sorted([a,b]))
#
# x, y = 'Z','B'
# ch =  sortChords(x,y)
# data = ('7/4',500)
# myDict[ch].append(data)
# myDict[ch].append(data)
# #print myDict

# print chords
# data = ('7/4',500)
# myDict[chords].append(data)
#
# print sorted(myDict[chords], key=lambda x: x[1])
