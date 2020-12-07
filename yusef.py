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
    deck.append("Joker")
    deck.append("Joker")
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

myDeck=shuffle_deck(build_deck())
# two players get five cards each
myHands=deal_hands(myDeck,2,5)

# draw from top
myTopCard=deal_top_card(myDeck)
while myTopCard[:2].strip() in ("Jo","A","2","3","4","5","6"):
    myDeck.append(myTopCard)
    myDeck=shuffle_deck(myDeck)
    myTopCard=deal_top_card(myDeck)

# player 1 goes