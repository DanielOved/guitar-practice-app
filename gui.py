#! /usr/bin/python2.7

import Tkinter as tk
from timer import Timer
from datetime import date
from chord import ChordPairSet, ChordPair
import json

class GUI():
    def __init__(self):
        #initialize the GUI itself
        self.root = tk.Tk()
        self.timer = Timer(5)
        self.chordNum = 0

        #get chordPair data from file
        filename = "data.json"
        with open(filename,"r") as f:
            chord_dict = json.loads(f.read())

        #generate all pairs and fill in data from file
        self.chordPS = ChordPairSet()
        self.chordPS.updateAllPairs(chord_dict)
        self.chordSet = self.chordPS.sortRecent()

        # Labels/Entries
        self.labelChord = tk.Label(text=self.chordSet[self.chordNum])
        self.labelTimer = tk.Label(text="0")
        self.entryVal   = tk.Entry(width=5)
        # Buttons
        self.start = tk.Button(text='Start', command=self.timer.start).grid(row=5,column=0)
        self.reset = tk.Button(text='Reset', command=self.timer.reset).grid(row=5,column=1)
        self.stop  = tk.Button(text='Pause', command=self.timer.stopTimer).grid(row=5,column=2)
        self.save  = tk.Button(text='Save',  command=self.saveEntry).grid(row=6,column=1)
        self.next  = tk.Button(text='Next',  command=self.next).grid(row=6,column=2)
        # Grid
        self.labelChord.grid(row=2)
        self.labelTimer.grid(row=4)
        self.entryVal.grid(row=6,column=0)
        # Functions
        self.updateTimer()
        self.root.mainloop()
        self.saveEntry()
        self.next()

    def next(self):
        self.chordNum += 1
        try:
            self.labelChord.configure(text=self.chordSet[self.chordNum])
        except IndexError:
            self.chordNum = 0
            self.labelChord.configure(text=self.chordSet[self.chordNum])

    def saveEntry(self):
        #update pair data
        thisChord = self.chordSet[self.chordNum]
        d = date.today().strftime("%m/%d")
        print d
        val = self.entryVal.get() #TODO: make sure it's an int
        self.chordPS.getPair(thisChord).add(val,d)
        print self.chordPS.getPair(thisChord)
        #save data
        fname2 = "data.json"
        self.chordPS.save(fname2)
        return

    def updateTimer(self):
        try:
            self.timer.start_time
        except AttributeError:
            self.root.after(1000, self.updateTimer)
        else:
            self.timer.update()
            elapsed = self.timer.get_seconds()
            self.labelTimer.configure(text=elapsed)
            self.root.after(1000, self.updateTimer)
