#! /usr/bin/python2.7

import Tkinter as tk
import csv #for saving, but might want to move this later
from timer import Timer

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.timer = Timer(5)
        self.chordNum = 0
        # Labels/Entries
        self.labelChord = tk.Label(text="getChords(self.chordNum)")
        self.labelTimer = tk.Label(text="0")
        self.entryVal   = tk.Entry(text="0",width=5)
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
            self.labelChord.configure(text="getChords(self.chordNum)")
        except IndexError:
            self.chordNum = 0
            self.labelChord.configure(text="getChords(self.chordNum)")

    def saveEntry(self):
        #print self.entryVal.get()
        chord1, chord2 = "getChords(self.chordNum)", "blank"
        data = [chord1, chord2, "7/3", self.entryVal.get()] #TODO: dynamic date
        with open(filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

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
