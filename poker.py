import numpy as np

class CARD:
    "Centralised Analytic Rateable Datapoint or CARD"
    def __init__(self, number,suit):
        self.number = number 
        self.suit = suit
        
    def output_suit(self):
        return {0:"Kreuz", 1:"Pik", 2:"Herz", 3:"Karo"}[self.suit]


class HAND:
    "Handsome Assorted Nominal Datacollection"
    def __init__(self, CARDs):
        self.CARDs = CARDs
        self.isPair = False
        self.isDoublePair = False
        self.isTriple = False
        self.isQuad = False
        self.isStreet = False
        self.isFlush = False
        self.isFullHouse = False
        self.isStreetFlush = False

        self.HANDValue  = 0

    def Value(self):
        self.numbers = []
        for i in self.CARDs:
            self.numbers += [i.number]

        self.duplicateDict = dict()
        for i in self.numbers:
            if i in self.duplicateDict:
                self.duplicateDict[i] += 1
            else:
                self.duplicateDict[i] =1
        
        self.duplicateArray = np.array(list(self.duplicateDict.items()))

        if 2 in self.duplicateArray[:,1]:
            self.isPair = True
        if 3 in self.duplicateArray[:,1]:
            self.isTriple = True
        if 4 in self.duplicateArray[:,1]:
            self.isQuad = True
        if 2 in self.duplicateArray[:,1] and 3 in self.duplicateArray[:,1]:
            self.isFullHouse = True
            self.isPair = False
        elif len(self.duplicateArray[:,1]) > 1:
            self.isDoublePair = True
            self.isPair = False
        
        self.tmp = 0
        for i in range(5):
            if self.CARDs[i].suit == self.CARDs[i-1].suit:
                self.tmp +=1
        if self.tmp == 5:
            self.isFlush = True
        
        
        if len(self.duplicateArray[:,0]) == 5:
            for i in self.duplicateArray[:,0]:
                if (i+1 in self.duplicateArray[:,0] and
                i+2 in self.duplicateArray[:,0] and
                i+3 in self.duplicateArray[:,0] and
                i+4 in self.duplicateArray[:,0]):
                    self.isStreet = True
        if self.isStreet == True and self.isFlush == True:
            self.isStreetFlush == True
            self.isStreet == False
            self.isFlush == False

        if self.isStreetFlush == True:
            self.HANDValue = max(self.duplicateArray[:,0]) * 16**9
        if self.isQuad == True:
            self.HANDValue = {v: k for k, v in self.duplicateDict.items()}[4] * 16**9 + {v: k for k, v in self.duplicateDict.items()}[1]

        

a = [CARD(10, 2) for i in range(4)] + [CARD(8,3)]
b = HAND(a)

b.Value()
print(b.isQuad)
print(b.HANDValue)