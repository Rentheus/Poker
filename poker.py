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
        elif len(self.duplicateArray[:,1]) > 1:
            self.isDoublePair = True
        #if 2 in self.duplicateArray[:,1]:
        #    self.isPair = True
        #if 2 in self.duplicateArray[:,1]:
        #    self.isPair = True


a = [CARD(10, 2) for i in range(4)]
b = HAND(a)
b.Value()
print(b.isPair)
print(b.isDoublePair)