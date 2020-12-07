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

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def drawHand(self,deck,numberCards):
        while numberCards!=0:
            self.hand.append(deck.drawCard())
            numberCards-=1
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()

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
deck.show()
print("\n---------\n")
deck.shuffle()
deck.show()
print("\n---------\n")
deck.drawCard().show()
print("\n---------\n")
emily=Player("Emily")
emily.drawHand(deck,5).showHand()
print("\n---------\n")
daniel=Player("Daniel")
daniel.drawHand(deck,5).showHand()

# drawing first card in yusef - must be >= 7
print("\n---------\n")
card=deck.drawCard()
while card.val < 7:
    deck.cards.append(card)
    deck.shuffle()
    card=deck.drawCard()
card.show()

# emily's turn