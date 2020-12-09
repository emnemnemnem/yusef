import pygame
from yusef import *
green = (0, 200, 50)

def show_hand(screen, player): # *** edit so i can show selected hand too
    """Displays all cards in hand of player on pygame display object"""
    x, y, space_between_cards = 5, 462, 5
    load_card_images(player)
    for card in player.hand:
        card.position_x, card.position_y = x, y
        card.rect=pygame.Rect(card.position_x,card.position_y,card.width,card.height)
        screen.blit(card.image, (x, y))
        x += card.width + space_between_cards

def select_card(player):
    """Player selects a card in hand to play"""
    print(player.selected_card)
    while player.selected_card is None:
        for card in player.hand:
            if card.isClicked():
                player.selected_card = card
    print(player.selected_card)

#def select_deck(player,mouse_x,mouse_y):
    """Player selects face-up or face-down deck"""


def load_card_images(player):
    "Loads image, and dimensions to card objects"
    for card in player.hand:
        card.image = pygame.image.load("deck/" + str(card.val) +"-"+str(card.suit)+".jpg")
        horizontal, vertical = card.image.get_size()
        card.width = horizontal
        card.height = vertical

def play_selected_card(screen, player):
    """Display card that is selected on pygame display object"""
    x = player.selected_card.position_x = 220
    y = player.selected_card.position_y
    screen.blit(player.selected_card.image, (x,y))

def show_winner(screen, player1, player2, my_font):
    """Display text stating game winner at end of game"""
    screen.fill(green)
    winner = str(player1) if player1.score > player2.score else str(player2)
    textsurface = my_font.render("The winner is: " + winner, False, (0, 0, 0))
    screen.blit(textsurface, (100, 270))

def update_selected_card_position(player, new_y_position):
    """Change the Y position of selected card to move card to played position"""
    if player.selected_card:
        player.selected_card.position_y = new_y_position

def evaluate(player1, player2):
    """determines who won round and updates their score"""
    round_winner = None
    if player1.selected_card and player2.selected_card:
        pygame.time.delay(1000)
        round_winner = player1 if player1.selected_card > player2.selected_card else player2
        round_winner.score += 1
        player1.selected_card, player2.selected_card = None, None
    return round_winner

def show_player_scores(screen, player1, player2):
    """Left corner is player 1 score, right corner is player 2 score"""
    font_size = 12
    my_font = pygame.font.SysFont('Times New Roman', font_size)
    textsurface1 = my_font.render("Player 1 score: " + str(player1.score), False, (0, 0, 0))
    textsurface2 = my_font.render("Player 2 score: " + str(player2.score), False, (0, 0, 0))
    screen.blit(textsurface1, (0,0))
    screen.blit(textsurface2, (470,0))

def getCoords(x,y):
    return [x,y]

def turn(player):
    print("start turn")
    select_card(player)
    print("finish turn")
    #player.swapCards([player.selected_card],deck.drawCard())
    #update_selected_card_position(player, new_y_position)
    #player.done=True
    #player.selected_card=None

def winner_goes_first(winner, loser):
    """Sets the winner to the starter of the next round"""
    winner.turn = True
    loser.turn = False

def main():
    sc_width, sc_height = 600, 555
    font_size = 30

    game=Game()
    game.start()
    print("Game has started")
    firstCard=game.deck.faceUp[0]
    firstCard.image=pygame.image.load("deck/" + str(firstCard.val) +"-"+str(firstCard.suit)+".jpg")
    face_down=game.deck.cards[len(game.deck.cards)-1]
    face_down.image=pygame.image.load("deck/face-down.jpg")

    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((sc_width, sc_height))

    for player in game.players:
        load_card_images(player)
    print("finished loading card images")

    pygame.font.init()
    my_font = pygame.font.SysFont('Times New Roman', font_size)

    #Main Game Loop
    game_is_running = True
    yusef_button=button((128,128,128),450,500,150,50,'Call yusef')
    swapped=1
    while game_is_running:
        screen.fill((252,204,210))
        screen.blit(firstCard.image, (300, 200))
        firstCard.position_x, firstCard.position_y = 300, 200
        horizontal, vertical = firstCard.image.get_size()
        firstCard.width = horizontal
        firstCard.height = vertical
        firstCard.rect=pygame.Rect(firstCard.position_x,firstCard.position_y,firstCard.width,firstCard.height)

        screen.blit(face_down.image, (200, 200))
        face_down.position_x, face_down.position_y = 200, 200
        horizontal, vertical = face_down.image.get_size()
        face_down.width = horizontal
        face_down.height = vertical
        face_down.rect=pygame.Rect(face_down.position_x,face_down.position_y,face_down.width,face_down.height)

        yusef_button.draw(screen)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game_is_running = False
                quit()

        for player in game.players:
            if player.turn:
                show_hand(screen, player)
                if swapped==0:
                    pygame.time.wait(1000)
                    screen.fill((0,0,0))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    game.switch_turn()
                    swapped=1
                    break
                for event in events:
                    pos = pygame.mouse.get_pos()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if yusef_button.isOver(pos):
                            game.call_yusef(player)
                            print("yusef button clicked")
                            pygame.time.wait(2000)
                            game_is_running=False
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        # get a list of all sprites that are under the mouse cursor
                        clicked_cards = [c for c in player.hand if c.rect.collidepoint(pos)]
                        for c in clicked_cards:
                            if len(player.selected_card)>0 and c.val == player.selected_card[0].val:
                                if c not in player.selected_card:
                                    player.selected_card.append(c)
                            else:
                                player.selected_card=[c]
                        if firstCard.rect.collidepoint(pos):
                            player.swap_cards(game.deck,False)
                            load_card_images(player)
                            screen.fill((252,204,210))
                            show_hand(screen,player)
                            firstCard=game.deck.faceUp[len(game.deck.faceUp)-1]
                            firstCard.image=pygame.image.load("deck/" + str(firstCard.val) +"-"+str(firstCard.suit)+".jpg")
                            swapped-=1
                        elif face_down.rect.collidepoint(pos):
                            player.swap_cards(game.deck,True)
                            load_card_images(player)
                            screen.fill((252,204,210))
                            show_hand(screen,player)
                            firstCard=game.deck.faceUp[len(game.deck.faceUp)-1]
                            firstCard.image=pygame.image.load("deck/" + str(firstCard.val) +"-"+str(firstCard.suit)+".jpg")
                            face_down=game.deck.cards[len(game.deck.cards)-1]
                            face_down.image=pygame.image.load("deck/face-down.jpg")
                            swapped-=1
                        
                #turn(player)
                #print("player turn")
                #if player.done:
                    #game.switchTurn()
                    #player.done=False

        #show_player_scores(screen, player1, player2)
        pygame.display.update()

        #winner = evaluate(player1,player2)
        # if winner:
        #     if winner == player1:
        #         winner_goes_first(player1, player2)
        #     else:
        #         winner_goes_first(player2, player1)

        # if not player1.hand and not player2.hand:
        #     show_winner(screen, player1, player2, my_font)
        #     pygame.display.update()
        #     pygame.time.delay(delay_time_ms)
        #     game_is_running = False

if __name__ == '__main__':
    main()