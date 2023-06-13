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
            join_menu(surface, text_1, text_2, text_3, text_4, text_5, text_6, teams)
        elif click_quit:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
    
def button(surface, xheight, yheight, xlength, ylength, buttontext):
    click = False
    button_rect = pygame.Rect(xheight, yheight, xlength, ylength)
    button_surface = pygame.Surface((button_rect.size))
    button_surface.fill(WHITE)
    pygame.draw.rect(button_surface, BLACK, button_surface.get_rect(), 5) #change the button thickness later
    button_tourney_text = font2.render(str(buttontext), True, BLACK)
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
        button_tourney_text = font2.render(str(buttontext), True, BLACK)
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
        button(surface, top_x - 10, top_y + level_height//2, 20, level_height//2 + 2, "PLACEHOLDER")
        for i in range(len(player_list)):
            button(surface, top_x - 10, top_y + level_height//2, 100, level_height//2 + 2, player_list[i])
                #upon opening and closing the host menu, the amount of brackets doubles. fix pls
                #also, upon entering a name in join menu and going into host menu, the box rapidly switches between the name and "no entrant"
    else:
        pygame.draw.line(surface, BLACK, (top_x, top_y), (top_x, top_y + height//2), 2)
        button(surface, top_x - 10, top_y + height//2, 20, height//2 + 2, "PLACEHOLDER")
        button(surface, top_x - 10, top_y + height//2, 100, height//2 + 2, "No Participants ")

def next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n))

def join_menu(surface, text_1, text_2, text_3, text_4, text_5, text_6, teams):
    text_editing_1 = False
    text_editing_2 = False
    text_editing_3 = False
    text_editing_4 = False
    text_editing_5 = False
    text_editing_6 = False
    while True:
        surface.fill(WHITE)
        PLAY_TEXT = font1.render("Join Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        INSTRUCT_TEXT = font3.render("Press 'enter' to confirm your team", True, BLACK)
        INSTRUCT_RECT = INSTRUCT_TEXT.get_rect(center=(640, 160))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        surface.blit(INSTRUCT_TEXT, INSTRUCT_RECT)
        text_rect_1 = pygame.Rect(400, 200, 500, 50)
        text_rect_2 = pygame.Rect(400, 275, 500, 50)
        text_rect_3 = pygame.Rect(400, 350, 500, 50)
        text_rect_4 = pygame.Rect(400, 425, 500, 50)
        text_rect_5 = pygame.Rect(400, 500, 500, 50)
        text_rect_6 = pygame.Rect(400, 575, 500, 50)
        text_surface_1 = pygame.Surface((text_rect_1.width, text_rect_1.height))
        text_surface_2 = pygame.Surface((text_rect_2.width, text_rect_2.height))
        text_surface_3 = pygame.Surface((text_rect_3.width, text_rect_3.height))
        text_surface_4 = pygame.Surface((text_rect_4.width, text_rect_4.height))
        text_surface_5 = pygame.Surface((text_rect_5.width, text_rect_5.height))
        text_surface_6 = pygame.Surface((text_rect_6.width, text_rect_6.height))
        text_surface_1.fill(WHITE)
        text_surface_2.fill(WHITE)
        text_surface_3.fill(WHITE)
        text_surface_4.fill(WHITE)
        text_surface_5.fill(WHITE)
        text_surface_6.fill(WHITE)
        pygame.draw.rect(text_surface_1, BLACK, text_surface_1.get_rect(), 5)
        pygame.draw.rect(text_surface_2, BLACK, text_surface_2.get_rect(), 5)
        pygame.draw.rect(text_surface_3, BLACK, text_surface_3.get_rect(), 5)
        pygame.draw.rect(text_surface_4, BLACK, text_surface_4.get_rect(), 5)
        pygame.draw.rect(text_surface_5, BLACK, text_surface_5.get_rect(), 5)
        pygame.draw.rect(text_surface_6, BLACK, text_surface_6.get_rect(), 5)
        mouse_pos = pygame.mouse.get_pos()
        if text_rect_1.collidepoint(mouse_pos):
            text_surface_1.fill(GREY)
            pygame.draw.rect(text_surface_1, BLACK, text_surface_1.get_rect(), 5)
        if text_rect_2.collidepoint(mouse_pos):
            text_surface_2.fill(GREY)
            pygame.draw.rect(text_surface_2, BLACK, text_surface_2.get_rect(), 5)
        if text_rect_3.collidepoint(mouse_pos):
            text_surface_3.fill(GREY)
            pygame.draw.rect(text_surface_3, BLACK, text_surface_3.get_rect(), 5)
        if text_rect_4.collidepoint(mouse_pos):
            text_surface_4.fill(GREY)
            pygame.draw.rect(text_surface_4, BLACK, text_surface_4.get_rect(), 5)
        if text_rect_5.collidepoint(mouse_pos):
            text_surface_5.fill(GREY)
            pygame.draw.rect(text_surface_5, BLACK, text_surface_5.get_rect(), 5)
        if text_rect_6.collidepoint(mouse_pos):
            text_surface_6.fill(GREY)
            pygame.draw.rect(text_surface_6, BLACK, text_surface_6.get_rect(), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect_1.collidepoint(event.pos):
                    text_editing_1 = True
                elif not text_rect_1.collidepoint(event.pos):
                    text_editing_1 = False
                    
                if text_rect_2.collidepoint(event.pos):
                    text_editing_2 = True
                elif not text_rect_2.collidepoint(event.pos):
                    text_editing_2 = False
                    
                if text_rect_3.collidepoint(event.pos):
                    text_editing_3 = True
                elif not text_rect_3.collidepoint(event.pos):
                    text_editing_3 = False
                    
                if text_rect_4.collidepoint(event.pos):
                    text_editing_4 = True
                elif not text_rect_4.collidepoint(event.pos):
                    text_editing_4 = False
                    
                if text_rect_5.collidepoint(event.pos):
                    text_editing_5 = True
                elif not text_rect_5.collidepoint(event.pos):
                    text_editing_5 = False
                    
                if text_rect_6.collidepoint(event.pos):
                    text_editing_6 = True
                elif not text_rect_6.collidepoint(event.pos):
                    text_editing_6 = False
                    
            if event.type == pygame.KEYDOWN and text_editing_1:
                if event.key == pygame.K_BACKSPACE:
                    text_1 = text_1[:-1]
                else:
                    text_1 += event.unicode
            if event.type == pygame.KEYDOWN and text_editing_2:
                if event.key == pygame.K_BACKSPACE:
                    text_2 = text_2[:-1]
                else:
                    text_2 += event.unicode
            if event.type == pygame.KEYDOWN and text_editing_3:
                if event.key == pygame.K_BACKSPACE:
                    text_3 = text_3[:-1]
                else:
                    text_3 += event.unicode
            if event.type == pygame.KEYDOWN and text_editing_4:
                if event.key == pygame.K_BACKSPACE:
                    text_4 = text_4[:-1]
                else:
                    text_4 += event.unicode
            if event.type == pygame.KEYDOWN and text_editing_5:
                if event.key == pygame.K_BACKSPACE:
                    text_5 = text_5[:-1]
                else:
                    text_5 += event.unicode
            if event.type == pygame.KEYDOWN and text_editing_6:
                if event.key == pygame.K_BACKSPACE:
                    text_6 = text_6[:-1]
                else:
                    text_6 += event.unicode
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    team_list = [text_1, text_2, text_3, text_4, text_5, text_6]
                    join_input_return(team_list)
                    confirmtext = "Players Added:"
                    CONFIRM_TEXT = font2.render(confirmtext, True, BLACK)
                    CONFIRM_1 = font2.render(text_1, True, BLACK)
                    CONFIRM_2 = font2.render(text_2, True, BLACK)
                    CONFIRM_3 = font2.render(text_3, True, BLACK)
                    CONFIRM_4 = font2.render(text_4, True, BLACK)
                    CONFIRM_5 = font2.render(text_5, True, BLACK)
                    CONFIRM_6 = font2.render(text_6, True, BLACK)
                    CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(640, 200))
                    CONFIRM_RECT1 = CONFIRM_1.get_rect(center=(640, 250))
                    CONFIRM_RECT2 = CONFIRM_2.get_rect(center=(640, 300))
                    CONFIRM_RECT3 = CONFIRM_3.get_rect(center=(640, 350))
                    CONFIRM_RECT4 = CONFIRM_4.get_rect(center=(640, 400))
                    CONFIRM_RECT5 = CONFIRM_5.get_rect(center=(640, 450))
                    CONFIRM_RECT6 = CONFIRM_6.get_rect(center=(640, 500))
                    surface.blit(CONFIRM_TEXT, CONFIRM_RECT)
                    surface.blit(CONFIRM_1, CONFIRM_RECT1)
                    surface.blit(CONFIRM_2, CONFIRM_RECT2)
                    surface.blit(CONFIRM_3, CONFIRM_RECT3)
                    surface.blit(CONFIRM_4, CONFIRM_RECT4)
                    surface.blit(CONFIRM_5, CONFIRM_RECT5)
                    surface.blit(CONFIRM_6, CONFIRM_RECT6)
                    text_1 = ""
                    text_2 = ""
                    text_3 = ""
                    text_4 = ""
                    text_5 = ""
                    text_6 = ""
                    teams += 1
                    pygame.display.update()
                    pygame.time.delay(2000)  # Delay in milliseconds
                    surface.fill(WHITE)
                    
        click_back = button(surface, 40, 650, 100, 50, "Back")
        if click_back:
            main_menu(surface, teams)
        input_text_1 = font2.render(text_1, True, BLACK)
        input_rect_1 = input_text_1.get_rect(center=text_rect_1.center)
        input_text_2 = font2.render(text_2, True, BLACK)
        input_rect_2 = input_text_2.get_rect(center=text_rect_2.center)
        input_text_3 = font2.render(text_3, True, BLACK)
        input_rect_3 = input_text_3.get_rect(center=text_rect_3.center)
        input_text_4 = font2.render(text_4, True, BLACK)
        input_rect_4 = input_text_4.get_rect(center=text_rect_4.center)
        input_text_5 = font2.render(text_5, True, BLACK)
        input_rect_5 = input_text_5.get_rect(center=text_rect_5.center)
        input_text_6 = font2.render(text_6, True, BLACK)
        input_rect_6 = input_text_6.get_rect(center=text_rect_6.center)
        surface.blit(text_surface_1, text_rect_1)
        surface.blit(input_text_1, input_rect_1)
        surface.blit(text_surface_2, text_rect_2)
        surface.blit(input_text_2, input_rect_2)
        surface.blit(text_surface_3, text_rect_3)
        surface.blit(input_text_3, input_rect_3)
        surface.blit(text_surface_4, text_rect_4)
        surface.blit(input_text_4, input_rect_4)
        surface.blit(text_surface_5, text_rect_5)
        surface.blit(input_text_5, input_rect_5)
        surface.blit(text_surface_6, text_rect_6)
        surface.blit(input_text_6, input_rect_6)
        pygame.display.update()

def join_input_return(text):
    teamX = text
    print(teamX)
    # ruban's player input code will go here
    player_list.append(teamX)
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
text_1 = ""
text_2 = ""
text_3 = ""
text_4 = ""
text_5 = ""
text_6 = ""
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