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

def update_selected_card_position(card, new_y_position):
    """Change the Y position of selected card to move card to played position"""
    card.position_y = new_y_position

def show_player_scores(screen, players):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    for i,player in enumerate(players):
        score = myfont.render(str(player.name)+" score: " + str(player.score), False, (0, 0, 0))
        screen.blit(score, (300,(i+1)*100))
    pygame.display.update()

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
    turns=10000 # ***for testing purposes... change to 0 later
    threshold=3*game.num_players
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
                myfont = pygame.font.SysFont('Comic Sans MS', 30)
                textsurface = myfont.render(player.name+"'s turn", False, (0, 0, 0))
                screen.blit(textsurface,(100,400))
                show_hand(screen, player)
                if swapped==0:
                    pygame.time.wait(1000)
                    screen.fill((0,0,0))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    game.switch_turn()
                    turns+=1
                    swapped=1
                    break
                for event in events:
                    pos = pygame.mouse.get_pos()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if yusef_button.isOver(pos):
                            if turns<=threshold:
                                font = pygame.font.SysFont('Comic Sans MS', 20)
                                textsurface = font.render("Cannot call yusef before three rounds are over", False, (0, 0, 0))
                                screen.blit(textsurface,(50,300))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                break
                            else:
                                game.call_yusef(player,screen)
                                pygame.time.wait(2000)
                                play=True
                                while play:
                                    show_player_scores(screen,game.players)
                                    play_again_button=button((128,128,128),450,300,150,50,'Play again')
                                    play_again_button.draw(screen)
                                    pygame.display.update()
                                    for ev in events:
                                        pos = pygame.mouse.get_pos()
                                        if event.type==pygame.MOUSEBUTTONDOWN:
                                            if play_again_button.isOver(pos):
                                                play=False
                                                game.play_again()
                                #game_is_running=False
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        # get a list of all sprites that are under the mouse cursor
                        clicked_cards = [c for c in player.hand if c.rect.collidepoint(pos)]
                        for c in clicked_cards:
                            if len(player.selected_card)>0 and c.val == player.selected_card[0].val:
                                if c not in player.selected_card:
                                    player.selected_card.append(c)
                                    update_selected_card_position(c,400)
                            else:
                                if len(player.selected_card)>0:
                                    for c in player.selected_card:
                                        update_selected_card_position(c,462)
                                player.selected_card=[c]
                                update_selected_card_position(c,400)
                        if firstCard.rect.collidepoint(pos):
                            if len(player.selected_card)==0:
                                font = pygame.font.SysFont('Comic Sans MS', 20)
                                textsurface = font.render("Please select a card from your deck", False, (0, 0, 0))
                                screen.blit(textsurface,(50,300))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                break
                            player.swap_cards(game.deck,False)
                            load_card_images(player)
                            screen.fill((252,204,210))
                            show_hand(screen,player)
                            firstCard=game.deck.faceUp[len(game.deck.faceUp)-1]
                            firstCard.image=pygame.image.load("deck/" + str(firstCard.val) +"-"+str(firstCard.suit)+".jpg")
                            swapped-=1
                        elif face_down.rect.collidepoint(pos):
                            if len(player.selected_card)==0:
                                font = pygame.font.SysFont('Comic Sans MS', 20)
                                textsurface = font.render("Please select a card from your deck", False, (0, 0, 0))
                                screen.blit(textsurface,(50,300))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                break
                            player.swap_cards(game.deck,True)
                            load_card_images(player)
                            screen.fill((252,204,210))
                            show_hand(screen,player)
                            firstCard=game.deck.faceUp[len(game.deck.faceUp)-1]
                            firstCard.image=pygame.image.load("deck/" + str(firstCard.val) +"-"+str(firstCard.suit)+".jpg")
                            face_down=game.deck.cards[len(game.deck.cards)-1]
                            face_down.image=pygame.image.load("deck/face-down.jpg")
                            swapped-=1

        pygame.display.update()

if __name__ == '__main__':
    main()