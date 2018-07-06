#! /usr/bin/python2.7

import Tkinter as tk
from timer import Timer
from datetime import date
from chord import ChordPairSet, ChordPair
import json
from PIL import Image, ImageTk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class GUI():
    def __init__(self):
        #initialize the GUI itself
        self.root = tk.Tk()
        self.root.title("One Minute Changes")
        bgColor = 'gray21'
        self.root.configure(bg=bgColor)
        self.timer = Timer(60)
        self.chordNum = 0

        #get chordPair data from file
        filename = "data.json"
        with open(filename,"r") as f:
            chord_dict = json.loads(f.read())

        #Framing
        topFrame = tk.Frame(self.root,bg=bgColor)
        topFrame.pack(side='top')
        timerFrame = tk.Frame(self.root,bg=bgColor)
        timerFrame.pack()
        botFrame = tk.Frame(self.root,bg=bgColor,pady='5')
        botFrame.pack()

        #generate all pairs and fill in data from file
        self.chordPS = ChordPairSet()
        self.chordPS.updateAllPairs(chord_dict)
        self.chordSet = self.chordPS.sortRecent()

        # Labels/Entries
        self.labelChord = tk.Label(topFrame, text=self.chordSet[self.chordNum],
                        font=("Courier", 20),bg=bgColor,fg='white',pady='5',wraplength='200')
        self.labelTimer = tk.Label(timerFrame,text="60",font=("Courier", 44),bg=bgColor)
        self.labelTimer.pack(side='top')

        self.entryVal   = tk.Entry(botFrame,width=2,bg='lavender',highlightbackground=bgColor,) #TODO: add int validation
        self.entryVal.pack(side='top',fill='x')

        # Icons
        startImg = Image.open('./images/play.png')
        startImg = startImg.resize((25, 25))
        startIm = ImageTk.PhotoImage(startImg)
        pauseImg = Image.open('./images/pause.png')
        pauseImg = pauseImg.resize((25, 25))
        pauseIm = ImageTk.PhotoImage(pauseImg)
        stopImg = Image.open('./images/stop.png')
        stopImg = stopImg.resize((25, 25))
        stopIm = ImageTk.PhotoImage(stopImg)
        fwImg = Image.open('./images/fw_arrow')
        fwImg = fwImg.resize((25, 25))
        fwIm = ImageTk.PhotoImage(fwImg)
        bwImg = Image.open('./images/bw_arrow')
        bwImg = bwImg.resize((25, 25))
        bwIm = ImageTk.PhotoImage(bwImg)

        # f = Figure(figsize=(5,5), dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        # self.canvas = FigureCanvasTkAgg(f)
        # self.canvas.show()
        # self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)
        # # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # # toolbar.update()
        # self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Buttons
        self.start = tk.Button(timerFrame, image=startIm,
                    width="20",height="20",bg='seagreen2',fg='black',relief='flat',
                    highlightbackground=bgColor, command=self.timer.start).pack(side='left')
        self.reset = tk.Button(timerFrame, image=stopIm,
                    width="20",height="20",bg='palevioletred3', fg='black',relief='flat',
                    highlightbackground=bgColor, command=self.timer.reset).pack(side='right')
        self.stop  = tk.Button(timerFrame, image=pauseIm,
                    width="20",height="20",bg='lightsteelblue2',fg='black',relief='flat',
                    highlightbackground=bgColor, command=self.timer.stopTimer).pack()
        self.save  = tk.Button(botFrame, text='Save',
                    bg='slategray1',fg='black',relief='flat',
                    highlightbackground=bgColor,command=self.saveEntry).pack(side="bottom",fill='x')
        self.next  = tk.Button(topFrame, image=fwIm,
                    width="50",height="25", bg=bgColor,fg='black',relief='flat',
                    highlightbackground=bgColor,command=self.next).pack(side='right',fill='x')
        self.prev  = tk.Button(topFrame,image=bwIm,
                    width="50",height="25",bg=bgColor,fg='black', relief='flat',
                    highlightbackground=bgColor, command=self.prev).pack(side='left',fill='x')

        # Delayed Packing
        self.labelChord.pack(side='top')

        # Functions
        self.updateTimer()
        self.root.mainloop()


    #def showGraph(self):


    def next(self):
        self.chordNum += 1
        try:
            self.labelChord.configure(text=self.chordSet[self.chordNum])
        except IndexError:
            self.chordNum = 0
            self.labelChord.configure(text=self.chordSet[self.chordNum])

    def prev(self):
        self.chordNum -= 1
        try:
            self.labelChord.configure(text=self.chordSet[self.chordNum])
        except IndexError:
            self.chordNum = len(self.chordSet)-1
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
