#! /usr/bin/python2.7

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import chord
import json


import Tkinter as Tk

#get chordPair data from file
filename = "data.json"
with open(filename,"r") as f:
    chord_dict = json.loads(f.read())

chordPS = chord.ChordPairSet()
chordPS.updateAllPairs(chord_dict)
chordSet = chordPS.sortRecent()

print chordSet[-1]['history']

class Chart():
    def showChart(self, master,obj): #TODO: include x and y data
        self.frame = Tk.Frame(master)
        self.f = Figure( figsize=(5, 5), dpi=80 )
        self.ax0 = self.f.add_axes( (.125, .125, .75, .75), axisbg=(.75,.75,.75),frameon=True)
        self.ax0.set_xlabel( 'Date' )
        self.ax0.set_ylabel( 'Chord Changes' )
        #self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")


        self.frame = Tk.Frame( root )
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame )
        self.toolbar.pack()
        self.toolbar.update()

        def plotPair(self):
            self.ax0.plot(x,y)
            return

        def plotAllPairs(self):
            return


if __name__ == '__main__':
    root = Tk.Tk()
    app = Chart(root,chordSet)
    root.title( "MatplotLib with Tkinter" )
    root.update()
    root.deiconify()
    root.mainloop()
