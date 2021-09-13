import numpy as np
import random

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
        elif 2 in self.duplicateArray[:,1] and 3 in self.duplicateArray[:,1]:
            self.isFullHouse = True
            self.isPair = False
            self.isTriple = False
        elif len(self.duplicateArray[:,1]) > 1 and len(self.duplicateArray[:,1]) < 4:
            self.isDoublePair = True
            self.isPair = False
        
        self.tmp = 0
        for i in range(5):
            if self.CARDs[i].suit == self.CARDs[i-1].suit:
                self.tmp +=1
        if self.tmp == 5:
            self.isFlush = True
        
        ########################################### HANDValue basiert auf 13-er System da es 13 Verschiedene Karten gibt
        #  Value ergibt sich so: Value der Kombinationskarten* Kombinationswert^13 + Nächsthöchste Karte
        ########################################### HANDValue basiert auf 13-er System da es 13 Verschiedene Karten gibt
        # #  Value ergibt sich so: Value der Kombinationskarten* Kombinationswert^13 + Nächsthöchste Karte        
        
        if len(self.duplicateArray[:,0]) == 5:
            for i in self.duplicateArray[:,0]:
                if (i+1 in self.duplicateArray[:,0] and
                i+2 in self.duplicateArray[:,0] and
                i+3 in self.duplicateArray[:,0] and
                (i+4 in self.duplicateArray[:,0] or (i-1 == 1 and 13 in self.duplicateArray[:,0]))):
                    self.isStreet = True
        if self.isStreet == True and self.isFlush == True:
            self.isStreetFlush == True
            self.isStreet == False
            self.isFlush == False

        print([k for k,v in self.duplicateDict.items()])

        if self.isStreetFlush == True:
            self.HANDValue = max(self.duplicateArray[:,0]) * 13**9
        elif self.isQuad == True:
            self.HANDValue = {v: k for k, v in self.duplicateDict.items()}[4] * 13**8 + {v: k for k, v in self.duplicateDict.items()}[1]
        elif self.isFullHouse == True:
            self.HANDValue = {v: k for k, v in self.duplicateDict.items()}[3] * 13**7 + {v: k for k, v in self.duplicateDict.items()}[2] * 13**3
        elif self.isFlush == True:
            self.HANDValue = 2*13**6
        elif self.isStreet == True:
            self.HANDValue == max(self.duplicateArray[:,0]) * 13**5
        elif self.isTriple == True:
            self.HANDValue = [k for k,v in self.duplicateDict.items() if v == 3][0] * 13**4 + np.max([k for k,v in self.duplicateDict.items() if v ==1])
        elif self.isDoublePair == True:
            self.HANDValue = np.max([k for k,v in self.duplicateDict.items() if v == 2])* 13**3 + np.min([k for k,v in self.duplicateDict.items() if v == 2]) * 13**1 + np.max([k for k,v in self.duplicateDict.items() if v ==1])
        elif self.isPair == True:
            self.HANDValue = [k for k,v in self.duplicateDict.items() if v == 2][0] * 13**2 + np.max([k for k,v in self.duplicateDict.items() if v ==1])
        else:
            self.HANDValue = np.max([k for k,v in self.duplicateDict.items() if v ==1])

class game:
    def __init__(self):
        self.players = []
        self.deck = []
        for i in range(4):
            for j in range(13):
                self.deck.append(CARD(j,i))
  
    def chooseCARD(self):
        self.tempCARD = random.choice(self.deck)
        self.deck.remove(self.tempCARD)
        return self.tempCARD


        
a = game()
print(len(a.deck))
#a = [CARD(i+3, 2) for i in range(4)] + [CARD(13,3)]
#b = HAND(a)
##c = [CARD(np.random.randint(2,14), np.random.randint(1,5)) for i in range(5)]
##d = HAND(c)
##d.Value()
##
#b.Value()
##print(b.isTriple)
##print(b.HANDValue > d.HANDValue)
#print(b.isStreet)
##print(d.HANDValue)

