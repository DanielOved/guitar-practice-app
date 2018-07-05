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
    print pair
    try:
        chord = chordDict.get(pair[0]).get(pair[1])
    except KeyError:
        return (None,None)
    else:
        scoreHi, scoreRecent = chord["best"], chord["recent"]
        return (scoreHi, scoreRecent)

def sortPairs(fullJson):
    #sorts all chord pairs by worst performance
    return fullJson

class Chord():
    self.getPairs()
    self.save()
    self.pairs = {}
    self.update()

    def __init__(self):
        self.pairs

    def getPair(self,chord):
        return self.pairs[chord]

    def getPairs(self):
        return self.pairs

    def update(self,chord):
        self.pairs[chord] = chord.pairs[self]

    def save(self):
        #should format to json and append to file
        return self.getPairs
