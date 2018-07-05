from sets import Set

allChords = ['A','Am','D','Dm','E','Em','C','G']

def generateData(chord1,chord2,count):
    #formats history and updates recent and/or best score for given chord pair
    return chord1,chord2,count,time.time()

def getPairs(dic):
    #lists all chord pairs (use a set) from a dict
    allpairs = set()
    bestD = {}
    recentD = {}
    for chord1 in allChords:
        if chord1 in dic.keys():
            for chord2 in allChords:
                if chord2 in dic[chord1]:
                    chord = dic[chord1][chord2]
                    scoreHi, scoreRecent = chord["best"], chord["recent"]
                    #new pair found, add it to the set
                    #sortPair = sorted((chord1,chord2))
                    sortPair = (chord1,chord2)
                    tup = (sortPair[0],sortPair[1])
                    allpairs.add(tup)
                    bestD[tup] = scoreHi
                    recentD[tup] = scoreRecent

    return allpairs,bestD,recentD

def getChordData(dic):
    chordData = set()
    for chord1 in allChords:
        if chord1 in dic.keys():
            for chord2 in allChords:
                if chord2 in dic[chord1]:
                    chord = dic[chord1][chord2]
                    scoreHi, scoreRecent = chord["best"], chord["recent"]
                    #new pair found, add it to the set
                    sortPair = sorted((chord1,chord2))
                    sortPair = (chord1,chord2)
                    tup = (sortPair[0],sortPair[1],scoreHi,scoreRecent)
                    chordData.add(tup)
    return chordData

def getPair(pair,chordDict):
    #returns copy of pair
    try:
        chord = chordDict.get(pair[0]).get(pair[1])
    except KeyError:
        return (None,None)
    else:
        scoreHi, scoreRecent, hist = chord["best"], chord["recent"], chord["history"]
        return pair, scoreHi, scoreRecent, hist

class ChordPairSet():
    def __init__(self):
        self.chords = sorted(allChords)
        self.allPairs = Set()
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

    def sortWorst(self, method=0):
        #sorts by worst high score (method=0) or worst recent score (method=1)
        return

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

    def save(self):
        return

class ChordPair(object):
    def __init__(self,chord1,chord2,best=0,recent=0,history=[]):
        self.chords = tuple(sorted((chord1,chord2)))
        self.best = best
        self.recent = recent
        self.history = history
        self.update()

    def __str__(self):
        return "{}: Best = {}, Recent = {}".format(self.chords,self.best,self.recent)

    def __hash__(self):
        return hash(self.chords)

    def __eq__(self,other):
        return(self.__class__ == other.__class__ and self.chords == other.chords)

    def __ne__(self,other):
        return(self.__class__ != other.__class__ and self.hash != other.hash)

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
        self.getBest()
        self.getRecent()
        return

    def add(self,count,date):
        self.history.append((count,date))
        self.update()
        return
