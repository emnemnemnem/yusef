from random import shuffle
import pygame

class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.val=val
        self.image=None
        self.width=None
        self.height=None
        self.position_x, self.position_y = 0,0
        self.rect=None
        self.selected=False

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

    def drawCard(self,face_down:bool): # from face-down pile
        if face_down is True:
            return self.cards.pop()
        elif face_down is False:
            return self.faceUp.pop()
    
    def drawFirstCard(self):
        card=self.drawCard(True)
        while card.val < 7:
            self.cards.append(card)
            self.shuffle()
            card=self.drawCard(True)
        self.faceUp.append(card)

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.duplicates=dict([])
        self.turn=False
        self.done=False
        self.selected_card=[] # list of selected cards
        self.score=0

    def drawHand(self,deck:Deck,numberCards:int,face_down:bool): # from face-down pile. eventually, *** i could make another parameter - true or false for face-down or face-up
        while numberCards!=0:
            drawn=deck.drawCard(face_down)
            self.hand.append(drawn)
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

    def swap_cards(self, deck:Deck, face_down:bool): 
        # puts toSwap onto face up, no matter what
        # either removes from face down or face up pile
        print("start swap")
        to_swap=self.selected_card # this is a list
        for card in to_swap:
            print("to_swap: "+str(card.show()))
            self.hand.remove(card)
        self.drawHand(deck,1,face_down)
        for card in to_swap:
            deck.faceUp.append(card)
        print("end swap")

class Game:
    def __init__(self):
        self.players = []
        self.deck=Deck()
        self.num_players=int(input("Input the number of players: \n"))
        for i in range(0,self.num_players):
            name=input("Input User {} Name: \n".format(i+1))
            self.players.append(Player(name))

    def start(self):
        self.deck.shuffle()
        for player in self.players:
            player.drawHand(self.deck,5,True)
        self.deck.drawFirstCard()
        self.players[0].turn=True

    def switch_turn(self):
        for i,player in enumerate(self.players):
            if player.turn:
                player.turn=not player.turn
                if i==len(self.players)-1:
                    self.players[0].turn=True
                else:
                    self.players[i+1].turn=True
                break

    def call_yusef(self,player,screen):
        self.update_scores()
        for compare in self.players:
            if compare==player:
                continue
            elif compare.score<=player.score:
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render(player.name+" loses", False, (0, 0, 0))
                screen.blit(textsurface,(100,400))
                pygame.display.update()
            else:
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render(player.name+" wins", False, (0, 0, 0))
                screen.blit(textsurface,(100,400))
                pygame.display.update()

    def update_scores(self):
        for player in self.players:
            for card in player.hand:
                player.score+=card.val

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False