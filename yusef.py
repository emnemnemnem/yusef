#two-player yusef
from random import shuffle

def build_deck() -> list:
    deck=[]
    suits=['Hearts','Diamonds','Clubs','Spades']
    for suit in suits:
        for i in range(1,14):
            if i==1:
                deck.append('A of '+suit)
            elif i == 11:
                deck.append('J of '+suit)
            elif i==12:
                deck.append('Q of '+suit)
            elif i==13:
                deck.append('K of '+suit)
            else:
                deck.append(str(i)+' of '+suit)
    return deck

def shuffle_deck(deck:list) -> list:
    shuffle(deck)
    return deck

def deal_top_card(deck:list) -> str:
    card=deck.pop()
    return card

def deal_hands(deck:list,numHands:int,sizeHand:int) -> list:
    hands=[]
    while numHands>0 and len(deck)>0:
        hand=[]
        origSizeHand=sizeHand
        while sizeHand>0 and len(deck)>0:
            hand.append(deck.pop())
            sizeHand-=1
        sizeHand=origSizeHand
        hands.append(hand)
        numHands-=1
    return hands

def get_sums(decks:list) -> list:
    sums=[]
    for i,deck in enumerate(decks):
        sumDeck=0
        for card in deck:
            value=card[:2].strip()
            if value=="A":
                sumDeck+=1
            elif value=="J":
                sumDeck+=10
            elif value=="Q":
                sumDeck+=10
            elif value=="K":
                sumDeck+=10
            else:
                sumDeck+=int(value)
        sums.append(sumDeck)
    return sums

myDeck=shuffle_deck(build_deck())
myFirstCard=deal_top_card(myDeck)
myHands=deal_hands(myDeck,2,5)
mySums=get_sums(myHands)
print(myHands)
print(mySums)