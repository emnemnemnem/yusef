#two-player yusef
from random import shuffle

def build_deck() -> list:
    deck=[]
    suits=['Hearts','Diamonds','Clubs','Spades']
    for suit in suits:
        for i in range(1,14):
            if i==1:
                deck.append('Ace of '+suit)
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

myDeck=shuffle_deck(build_deck())
myFirstCard=deal_top_card(myDeck)
myHands=deal_hands(myDeck,2,5)
print(myHands)