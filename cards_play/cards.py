import itertools
import random

deck = []

class CardsGame:
    def __init__(self):
        self.deck=[]
        typs = ["Spade", "Club", "Heart", "Diamond"]
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]

        for typ in typs:
            for num in nums:
                self.deck.append((typ, num))


   
    def shuffleCards(self):
        return random.shuffle(self.deck)
     
    def getTopCard(self):
        deck0 = self.deck[0]
        print('Here is a card from the top of the deck:', deck0)
        self.deck.remove(deck0)
        # print('Deck:',deck)
        if deck0 != None:
            return deck0
        elif deck0 == None:
            return 'No Cards left'

#getTopCard()

    def sortDeck(self,val):
        val = self.replaceFirst(val)
        s = []
        h = []
        d = []
        c = []
        for tpl in val:
            if tpl[0] == 'Spade':
                s.append(tpl)
            elif tpl[0] == 'Club':
                c.append(tpl)
            elif tpl[0] == 'Diamond':
                d.append(tpl)
            elif tpl[0] == 'Heart':
                h.append(tpl)
        s = self.sortNum(s)
        d = self.sortNum(d)
        h = self.sortNum(h)
        c = self.sortNum(c)
        s.extend(d)
        s.extend(h)
        s.extend(c)
        val = self.replaceLast(s)
        
        return val


    def sortNum(self, inArr):
        n = len(inArr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if inArr[j][1] > inArr[j+1][1]:
                    inArr[j], inArr[j+1] = inArr[j+1], inArr[j]
        return inArr


    def replaceFirst(self, inArr):
        n = len(inArr)
        for i in range(n):
            list1 = list(inArr[i])

            j = 0
            while j < len(list1):
                if(list1[j] == "jack"):
                    list1[j] = 11
                elif (list1[j] == "queen"):
                    list1[j] = 12
                elif (list1[j] == "king"):
                    list1[j] = 13
                elif (list1[j] == "ace"):
                    list1[j] = 14
                j = j + 1

            inArr[i] = tuple(list1)

        return inArr


    def replaceLast(self, inArr):
        n = len(inArr)
        for i in range(n):
            list1 = list(inArr[i])

            j = 0
            while j < len(list1):
                if(list1[j] == 14):
                    list1[j] = "ace"
                elif (list1[j] == 12):
                    list1[j] = "queen"
                elif (list1[j] == 13):
                    list1[j] = "king"
                elif (list1[j] == 11):
                    list1[j] = "jack"
                j = j + 1

            inArr[i] = tuple(list1)

        return inArr


    def playGame(self,nTurn):
        self.deck = self.replaceFirst(self.deck)
        print('--------------Lets Play------------')
        random.shuffle(self.deck)
        # shuffleCards()
        print('---------shuffling cards----------')
        player1 = 0
        player2 = 0
        v1 = 0

        for i in range(0, (nTurn*2)-1):
            
            if self.deck[i][0] == 'Club':
                v1 = 4
            elif self.deck[i][0] == 'Heart':
                v1 = 3
            elif self.deck[i][0] == 'Diamond':
                v1 = 2
            elif self.deck[i][0] == 'Spade':
                v1 = 1

            if i % 2 == 0:
                player1 += v1 * self.deck[i][1]
            else:
                player2 += v1 * self.deck[i][1]

        if player1 > player2:
            Winner = 'Player1'
            print('Winner:', Winner + '  Score:'+ str(player1))
        elif player2 > player1:
            Winner = 'Player2'
            print('Winner:', Winner + '  Score:'+ str(player2))


cg = CardsGame()
cg.shuffleCards()

print("Shuffeld cards -> ", cg.deck)

#cg.deck = cg.replaceFirst(cg.deck)
cg.deck = cg.sortDeck(cg.deck)
cg.deck = cg.replaceLast(cg.deck)
print("Sorted cards -> ", cg.deck)

cg.playGame(3)

    
