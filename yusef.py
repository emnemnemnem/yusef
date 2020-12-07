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
    

myDeck=shuffle_deck(build_deck())
myFirstCard=deal_top_card(myDeck)
print(myFirstCard)