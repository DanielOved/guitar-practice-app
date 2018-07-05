#! /usr/bin/python2.7

from gui import GUI
import pandas as pd
import chord
import jsonHelper as js
import json
from operator import itemgetter

#TODO: connect with GUI
#TODO: history charts
#TODO: function to validate data (no chars in count, sort the chord pairs so A->E and not E->A)
#TODO: metronome
#TODO: function to get worst scoring chords

#get chordPair data from file
filename = "data.json"
with open(filename,"r") as f:
    chord_dict = json.loads(f.read())

#generate all pairs and fill in data from file
chordPairs = chord.ChordPairSet()
chordPairs.updateAllPairs(chord_dict)
for p in chordPairs.allPairs:
    if p.best != 0:
        print p








# pairSet,pairBest,pairRecent = chord.getPairs(chord_dict)
#
# allPairs = set()
#
# for p in pairSet:
#     pair,best,recent,hist = chord.getPair(p,chord_dict)
#     ch = chord.ChordPair(pair[0],pair[1],best,recent,hist)
#     ch.getBest
#     print ch
#     allPairs.add(ch)
#
# print "\n\n\n"
#
# for pair in allPairs:
#     print pair


#gui=GUI()
