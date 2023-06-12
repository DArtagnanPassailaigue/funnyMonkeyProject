import pygame, sys
import math
import random
import os
def main_menu(surface, teams):
    while True:

        surface.fill(WHITE)

        menu_text = font1.render("Tournament Bracket Automation", True, BLACK)
        pygame.draw.rect(surface, BLACK, [0, 0, 1280, 720], 15)
        pygame.draw.rect(surface, BLACK, [0, 0, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [1230, 0, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [0, 670, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [1230, 670, 50, 50], 10)
        surface.blit(menu_text, (37, 100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Host rectangle 
        click_host = button(surface, 400, 250, 500, 100, "Host Tournament")  # Assign the menu state returned by the function
        # Join rectangle
        click_join = button(surface, 400, 400, 500, 100, "Join Tournament")  # Assign the menu state returned by the function
        # Quit rectangle
        click_quit = button(surface, 530, 550, 250, 75, "Quit")
        if click_host:
            host_menu(surface, teams)
        elif click_join:
            join_menu(surface, "", teams)
        elif click_quit:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
    
def button(surface, xheight, yheight, xlength, ylength, buttontext):
    click = False
    button_rect = pygame.Rect(xheight, yheight, xlength, ylength)
    button_surface = pygame.Surface((button_rect.size))
    button_surface.fill(WHITE)
    pygame.draw.rect(button_surface, BLACK, button_surface.get_rect(), 2) #change the button thickness later
    button_tourney_text = font2.render(buttontext, True, BLACK)
    button_text_centre = button_tourney_text.get_rect(center=button_surface.get_rect().center)
    button_surface.blit(button_tourney_text, button_text_centre)
        
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        button_hovering = True
    else:
        button_hovering = False
         
    if button_hovering:
        button_surface.fill(GREY)
        pygame.draw.rect(button_surface, BLACK, button_surface.get_rect(), 2) # change the button thickness later
        button_tourney_text = font2.render(buttontext, True, BLACK)
        button_text_centre = button_tourney_text.get_rect(center=button_surface.get_rect().center)
        button_surface.blit(button_tourney_text, button_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
        
    surface.blit(button_surface, button_rect)
    return click

def host_menu(surface, teams):
    teams = teams * 2
    while True:

        surface.fill(WHITE)

        PLAY_TEXT = font2.render("Host Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(100, 25))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        
        random.shuffle(player_list)
        draw_bracket(surface, teams, window_width // 2, 0, window_height, window_width // 2 - 100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        click_back = button(surface, 40, 650, 100, 50, "Back")
        if click_back:
            main_menu(surface, teams)

        pygame.display.update()    

def draw_bracket(surface, teams, top_x, top_y, height, width):
    if teams > 1:
        level_height = height // int(math.log2(teams))
        half_width = width // 2

        pygame.draw.line(surface, BLACK, (top_x, top_y + level_height), (top_x - half_width, top_y + level_height), 2)
        pygame.draw.line(surface, BLACK, (top_x, top_y + level_height), (top_x + half_width, top_y + level_height), 2)
        
        draw_bracket(surface, teams // 2, top_x - half_width, top_y + level_height, height - level_height, half_width)  # Adjust top_y here
        draw_bracket(surface, teams // 2, top_x + half_width, top_y + level_height, height - level_height, half_width)  # Adjust top_y here

        pygame.draw.line(surface, BLACK, (top_x, top_y), (top_x, top_y + level_height//2), 2)
        if len(player_list) % 2:
                player_list.append('No entrant')
        for i in range(len(player_list)):
            button(surface, top_x - 10, top_y + level_height//2, 100, level_height//2 + 2, player_list[i])
                #upon opening and closing the host menu, the amount of brackets doubles. fix pls
                #also, upon entering a name in join menu and going into host menu, the box rapidly switches between the name and "no entrant"
    else:
        pygame.draw.line(surface, BLACK, (top_x, top_y), (top_x, top_y + height//2), 2)
        button(surface, top_x - 10, top_y + height//2, 100, height//2 + 2, "No Participants ")

def next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n))

def join_menu(surface, text, teams):
    text_editing = False
    text_rect_height = 325
    boxnum = 0

    while True:
        surface.fill(WHITE)
        PLAY_TEXT = font1.render("Join Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        
        textbox(surface, 325)

        click_back = button(surface, 40, 650, 100, 50, "Back")
        click_add = button(surface, 500, 200, 300, 75, "+ Add Player")
        if click_back:
            main_menu(surface, teams)
        elif click_add:
            add_player_clicks += 1
            if add_player_clicks == 1:
                textbox(surface, 375)
            elif add_player_clicks == 3:
                textbox(surface, 425)
            elif add_player_clicks == 4:
                textbox(surface, 475)
            elif add_player_clicks == 5:
                textbox(surface, 525)
            elif add_player_clicks == 6:
                textbox(surface, 575)
            elif add_player_clicks == 7:
                textbox(surface, 625)
            elif add_player_clicks == 8:
                textbox(surface, 675)

        pygame.display.update()

def textbox(surface, height, text):
    text_rect = pygame.Rect(400, height, 500, 50)
    text_surface = pygame.Surface((text_rect.width, text_rect.height))
    text_surface.fill(WHITE)
    pygame.draw.rect(text_surface, BLACK, text_surface.get_rect(), 5)

    mouse_pos = pygame.mouse.get_pos()
    if text_rect.collidepoint(mouse_pos):
        text_surface.fill(GREY)
        pygame.draw.rect(text_surface, BLACK, text_surface.get_rect(), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                text_editing = True
            elif not text_rect.collidepoint(event.pos):
                text_editing = False

        if event.type == pygame.KEYDOWN and text_editing:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                join_input_return(text)
                CONFIRM_TEXT = font2.render("Player " + text + " added.", True, BLACK)
                CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(640, 200))
                surface.blit(CONFIRM_TEXT, CONFIRM_RECT)
                text = ""
                teams += 1
                pygame.display.update()
                pygame.time.delay(2000)  # Delay in milliseconds
                surface.fill(WHITE)
                
    input_text = font2.render(text, True, BLACK)
    input_rect = input_text.get_rect(center=text_rect.center)
    surface.blit(text_surface, text_rect)
    surface.blit(input_text, input_rect)
    
    pygame.display.update()
        
def join_input_return(text):
    player_list.append(text)
    fileName = folder + "players.csv"
    file = open(fileName,"a")    
    file.writelines("text")
    file.close  
    #make it so that the function will only add a name once it scans the file and sees that the name does not already exist
    #also make it so that on "win", the player.csv file is searched and the program appends ",Wins:(number of total wins)" next to the player's name

pygame.init()
pygame.font.init()
window_width, window_height = 1280, 720
window_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
folder = os.getcwd()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
font1 = pygame.font.SysFont(None, 111)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 30)
running = True
add_player_clicks = 0
text = ""
player_list = []
teams = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    mouse_state = pygame.mouse.get_pressed()
    main_menu(window_surface, teams)
    pygame.display.update()
    clock.tick(60)