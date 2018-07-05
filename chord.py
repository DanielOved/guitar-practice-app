import json

allChords = ['A','Am','D','Dm','E','Em','C','G']



class ChordPairSet():
    def __init__(self):
        self.chords = sorted(['A','Am','D','Dm','E','Em','C','G'])
        self.allPairs = set()
        self.createChordPairs()

    def getPair(self, pairId):
        for pair in self.allPairs:
            if pair == pairId:
                return pair
        return

    def updatePair(self,pairId,data):
        for d in data:
            self.getPair(pairId).add(d[0],d[1])
        return

    def sortRecent(self):
        #sorts by lowest recent score
        return sorted(self.allPairs, key=lambda x: x.recent)

    def sortBest(self):
        #sorts by lowest best score
        return sorted(self.allPairs, key=lambda x: x.best)

    def sortPairs(self):
        return sorted(self.allPairs, key=lambda x: x.chords)

    def createChordPairs(self):
        #generate set of all possible ChordPairs
        for chord1 in self.chords:
            for chord2 in self.chords:
                if chord2 != chord1:
                    newChord = ChordPair(chord1,chord2)
                    self.allPairs.add(newChord)
        return

    def updateAllPairs(self, dic):
            for chord1 in self.chords:
                if chord1 in dic.keys():
                    for chord2 in self.chords:
                        if chord2 in dic[chord1]:
                            #new data found for this pair, so lets update it
                            pairId = ChordPair(chord1,chord2)
                            existingChord = self.getPair(pairId)
                            data = dic[chord1][chord2]["history"]
                            self.updatePair(pairId, data)

    def save(self,filename):
        #turn chordPairs into json-able dict and saves it
        d = {}
        #print len(self.allPairs)
        sp = self.sortPairs()

        for ch in self.chords:
            d[ch] = {}

        for pair in sp:
            newEntry = pair.createDict()
            ch1, ch2 = pair.chords[0], pair.chords[1]
            d[ch1][ch2] = newEntry[ch1][ch2]

        with open(filename,"w") as f:
            json.dump(d,f,sort_keys=True,indent=1)
        return

class ChordPair(object):
    def __init__(self,chord1,chord2):
        self.chords = tuple(sorted((chord1,chord2)))
        self.best = 0
        self.recent = 0
        self.history = []
        self.update()

    def __str__(self):
        return "{}, {}:\nBest = {}, Recent = {}".format(self.chords[0],self.chords[1],self.best,self.recent,self.history)

    def __hash__(self):
        return hash(self.chords)

    def __eq__(self,other):
        return(self.__class__ == other.__class__ and self.chords == other.chords)

    def __ne__(self,other):
        return(self.__class__ != other.__class__ and self.chords != other.chords)

    def getRecent(self):
        if self.history != []:
            self.recent = self.history[-1][0]
            return self.recent
        return

    def getBest(self):
        for pt in self.history:
            if pt[0] > self.best:
                self.best = pt[0]
        return self.best

    def update(self):
        self.history = sorted(self.history, key = lambda x: x[1])
        self.getBest()
        self.getRecent()
        return

    def add(self,count,date):
        if not (count,date) in self.history:
            self.history.append((count,date))
            self.update()
        return

    def createDict(self):
        #turn pair into json-ready dict
        d = {}
        d[self.chords[0]]={self.chords[1]:
            {"best":self.best,
            "recent":self.recent,
            "history":[list(x) for x in self.history]}
            }
        return d
