#two-player yusef
from random import shuffle

class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.val=val

    def show(self):
        print("{} of {}".format(self.val,self.suit))

class Deck:
    def __init__(self):
        self.cards=[]
        self.faceUp=[]
        self.build()

    def build(self):
        suits=['Hearts','Diamonds','Clubs','Spades']
        for suit in suits:
            for i in range(1,14):
                self.cards.append(Card(suit,i))

    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()
    
    def drawFirstCard(self):
        card=deck.drawCard()
        while card.val < 7:
            deck.cards.append(card)
            deck.shuffle()
            card=deck.drawCard()
        self.faceUp.append(card)

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.duplicates=dict([])

    def drawHand(self,deck,numberCards):
        vals=set([])
        while numberCards!=0:
            drawn=deck.drawCard()
            self.hand.append(drawn)
            if drawn.val not in vals:
                vals.add(drawn.val)
            else:
                if drawn.val not in self.duplicates:
                    self.duplicates[drawn.val]=2
                else:
                    self.duplicates[drawn.val]+=1
                sorted(self.duplicates,reverse=True)
            numberCards-=1
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def duplicateVals(self): # returns boolean
        if self.duplicates is not None:
            return True
        else:
            return False
    
    def maxVal(self): # returns max value
        maximum=0
        for card in self.hand:
            if card.val > maximum:
                maximum=card.val
        return maximum

    def swapCards(self, toSwap:list, replaceWith:Card): # returns the cards that i put back onto deck pile
        for card in self.hand:
            if card in toSwap:
                self.hand.remove(card)
        self.hand.append(replaceWith)
        del self.duplicates[toSwap[0].val]
        return toSwap[0]

class Game:
    def __init__(self):
        self.players = []

    def start():
        deck = Deck()
        deck.shuffle()

def get_sums(decks:list) -> list:
    sums=[]
    for deck in decks:
        sumDeck=0
        for card in deck:
            value=card[:2].strip()
            if value=="A": sumDeck+=1
            elif value=="J": sumDeck+=10
            elif value=="Q": sumDeck+=10
            elif value=="K": sumDeck+=10
            elif value=="Jo": sumDeck+=0
            else: sumDeck+=int(value)
        sums.append(sumDeck)
    return sums

deck=Deck()
print("\n---------\n")
deck.shuffle()
deck.show()
print("\n---------\n")
emily=Player("Emily")
emily.drawHand(deck,5).showHand()
print("\n---------\n")
daniel=Player("Daniel")
daniel.drawHand(deck,5).showHand()

# drawing first card in yusef - must be >= 7
print("\n---------\n")

# emily's turn
# if emily.duplicateVals()==True and next(iter(emily.duplicates))*emily.duplicates[next(iter(emily.duplicates))] <= card:
#     # replace emily's duplicate values in hand with card
#     dup=next(iter(emily.duplicates))
#     swapOut=[]
#     for emily_card in emily.hand:
#         if emily_card.val==dup:
#             swapOut.append(emily_card)
#     card=emily.swapCards(swapOut,card)
