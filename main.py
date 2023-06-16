import pygame, sys
import math
import random
import os
# importing the necessary packages
def main_menu(surface, teams):
    '''Displays the main menu and manages access to the other functions through calling the "button()" function'''
    while True:
        # The graphic for the title screen, including the title and border design
        surface.fill(WHITE)
        menu_text = font1.render("Tournament Bracket Automation", True, BLACK)
        pygame.draw.rect(surface, BLACK, [0, 0, 1280, 720], 15)
        pygame.draw.rect(surface, BLACK, [0, 0, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [1230, 0, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [0, 670, 50, 50], 10)
        pygame.draw.rect(surface, BLACK, [1230, 670, 50, 50], 10)
        surface.blit(menu_text, (37, 100)) #confirms the assigned rectangles to be drawn to the surface
        # for loop that handles if the window is closed during this process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # Defining the host button as a variable
        click_host = button(surface, 400, 250, 500, 100, "Host Tournament")  # Assign the menu state returned by the function
        # Defining the join button as a variable
        click_join = button(surface, 400, 400, 500, 100, "Join Tournament")  # Assign the menu state returned by the function
        # Defining the quit button as a variable
        click_quit = button(surface, 530, 550, 250, 75, "Quit")
        # The button function becomes "true" when it's button is clicked, meaning that if it becomes true, the below code will run for the respective button clicked
        if click_host:
            host_menu(surface, teams)
        elif click_join:
            join_menu(surface, text_1, text_2, text_3, text_4, text_5, text_6, teams)
        elif click_quit:
            pygame.quit()
            sys.exit()
        # updates the display each run of the loop
        pygame.display.update()
    
def button(surface, xheight, yheight, xlength, ylength, buttontext):
    '''General function used for displaying the graphics for every button used and for detecting when the button is clicked'''
    click = False # sets click to False by default
    button_rect = pygame.Rect(xheight, yheight, xlength, ylength) #takes the given coordiantes in the function call
    button_surface = pygame.Surface((button_rect.size)) #finds the surface the button will occupy based on the provided coordinates
    button_surface.fill(WHITE) # fills exclusively the button surface with the colour white
    pygame.draw.rect(button_surface, BLACK, button_surface.get_rect(), 5) # draws a rectangle based on the size of the button surface and states the thickness of the border
    button_tourney_text = font2.render(str(buttontext), True, BLACK) # renders the button's provided text in the function call in "font 2", defined at the bottom of the code
    button_text_centre = button_tourney_text.get_rect(center=button_surface.get_rect().center) # centers the text onto the button
    button_surface.blit(button_tourney_text, button_text_centre)
        
    mouse_pos = pygame.mouse.get_pos() # constantly keeps track of the user's mouse
    # detects if the mouse is hovering over the button or not
    if button_rect.collidepoint(mouse_pos):
        button_hovering = True 
    else:
        button_hovering = False
         
    if button_hovering: # creates the effect of greying out the button when the user hovers over it
        # This is useful for the user to keep track of the location of their mouse without much effort
        button_surface.fill(GREY)
        pygame.draw.rect(button_surface, BLACK, button_surface.get_rect(), 2) # change the button thickness later
        button_tourney_text = font2.render(str(buttontext), True, BLACK)
        button_text_centre = button_tourney_text.get_rect(center=button_surface.get_rect().center)
        button_surface.blit(button_tourney_text, button_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
            # if the mouse is hovering and clicked, click is set to true for the button
        
    surface.blit(button_surface, button_rect)
    return click # return the boolean value of click
def host_menu(surface, teams):
    '''The menu that provides access to the tournament bracket, the main purpose of the program'''
    teams = teams * 2 # the "draw_bracket()" function divides the teams for an unknown reason, so this is here as a countermeasure
    while True:
        surface.fill(WHITE)
        # writes the host menu title text
        PLAY_TEXT = font2.render("Host Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(100, 25))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        # calls the "draw bracket" function, defined below, with the necessary default measurements
        draw_bracket(surface, teams, window_width // 2, 0, window_height, window_width // 2 - 100)
        # for loop in case the window is closed during this process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Defines the back button as a boolean variable
        click_back = button(surface, 40, 650, 100, 50, "Back")
        # if the button function assigned to back becomes true, the main menu will initiate
        if click_back:
            main_menu(surface, teams)
        pygame.display.update()  
          
def draw_bracket(surface, teams, top_x, top_y, height, width):
    '''This function draws a tournament bracket recursively.'''
    # `teams` is the total number of teams in the tournament, `top_x` and `top_y` are the top left coordinates 
    # of the bracket, `height` is the total height of the bracket, and `width` is the total width of the bracket.
    if teams > 1: # Check if there is more than one team left in this bracket
        level_height = height // int(math.log2(teams)) # Calculate the height of one level in the bracket
        half_width = width // 2 # Calculate the half width of the bracket

        # Draw the upper and lower horizontal lines of the bracket
        pygame.draw.line(surface, BLACK, (top_x, top_y + level_height), (top_x - half_width, top_y + level_height), 2)
        pygame.draw.line(surface, BLACK, (top_x, top_y + level_height), (top_x + half_width, top_y + level_height), 2)
        
        # Recursively draw the left and right half of the bracket
        draw_bracket(surface, teams // 2, top_x - half_width, top_y + level_height, height - level_height, half_width)  
        draw_bracket(surface, teams // 2, top_x + half_width, top_y + level_height, height - level_height, half_width)
        # Draw the vertical line of the bracket
        pygame.draw.line(surface, BLACK, (top_x, top_y), (top_x, top_y + level_height//2), 2)
            
        # Draw buttons for each player
        for i in range(len(player_list)):
            button(surface, top_x - 10, top_y + level_height//2, 100, level_height//2 + 2, player_list[i])
            
    else: # If there's only one or zero team left in this bracket
        # Draw the vertical line of the bracket
        pygame.draw.line(surface, BLACK, (top_x, top_y), (top_x, top_y + height//2), 2)
        # Draw the button for the team or "No Participants" if there's no team
        button(surface, top_x - 10, top_y + height//2, 100, height//2 + 2, "No Participants ")

def next_power_of_2(n):
    '''This function calculates the next power of 2 greater than or equal to n. '''
    # This is useful to determine the number of rounds in a tournament, as each round halves the number of teams.
    return 2 ** math.ceil(math.log2(n))

def join_menu(surface, text_1, text_2, text_3, text_4, text_5, text_6, teams):
    '''The menu that allows the names of the players on each team to be input, and counts the amount of teams participating'''
    # sets the text_editing variables to False, and establishes them as booleans
    text_editing_1 = False
    text_editing_2 = False
    text_editing_3 = False
    text_editing_4 = False
    text_editing_5 = False
    text_editing_6 = False
    while True:
        # draws the join menu title and instructive text
        surface.fill(WHITE)
        PLAY_TEXT = font1.render("Join Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        INSTRUCT_TEXT = font3.render("Press 'enter' to confirm your team", True, BLACK)
        INSTRUCT_RECT = INSTRUCT_TEXT.get_rect(center=(640, 160))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        surface.blit(INSTRUCT_TEXT, INSTRUCT_RECT)
        # establishes the rectangles for text to be typed into
        text_rect_1 = pygame.Rect(400, 200, 500, 50)
        text_rect_2 = pygame.Rect(400, 275, 500, 50)
        text_rect_3 = pygame.Rect(400, 350, 500, 50)
        text_rect_4 = pygame.Rect(400, 425, 500, 50)
        text_rect_5 = pygame.Rect(400, 500, 500, 50)
        text_rect_6 = pygame.Rect(400, 575, 500, 50)
        # establishes the surfaces for text to be typed into based on the above rectangles
        text_surface_1 = pygame.Surface((text_rect_1.width, text_rect_1.height))
        text_surface_2 = pygame.Surface((text_rect_2.width, text_rect_2.height))
        text_surface_3 = pygame.Surface((text_rect_3.width, text_rect_3.height))
        text_surface_4 = pygame.Surface((text_rect_4.width, text_rect_4.height))
        text_surface_5 = pygame.Surface((text_rect_5.width, text_rect_5.height))
        text_surface_6 = pygame.Surface((text_rect_6.width, text_rect_6.height))
        # fills the text input surfaces white
        text_surface_1.fill(WHITE)
        text_surface_2.fill(WHITE)
        text_surface_3.fill(WHITE)
        text_surface_4.fill(WHITE)
        text_surface_5.fill(WHITE)
        text_surface_6.fill(WHITE)
        # draws the text input rectangles based on the given properties above
        pygame.draw.rect(text_surface_1, BLACK, text_surface_1.get_rect(), 5)
        pygame.draw.rect(text_surface_2, BLACK, text_surface_2.get_rect(), 5)
        pygame.draw.rect(text_surface_3, BLACK, text_surface_3.get_rect(), 5)
        pygame.draw.rect(text_surface_4, BLACK, text_surface_4.get_rect(), 5)
        pygame.draw.rect(text_surface_5, BLACK, text_surface_5.get_rect(), 5)
        pygame.draw.rect(text_surface_6, BLACK, text_surface_6.get_rect(), 5)
        #gets the location of the mouse constantly
        mouse_pos = pygame.mouse.get_pos()
        # appplies the effect of greying out the text boxes upon hovering over them, for ease of use for the user
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
            # closes the program if the window is closed during this process
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # applies the status of "text_editing" to each text box upon clicking it
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
            
            # detects when a text box is typed into and gives the input to the "text_x" variable, removing the most recent character upon pressing backspace
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
            # upon pressing return: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # all of the text box contents will be sent to team_list
                    team_list = [text_1, text_2, text_3, text_4, text_5, text_6]
                    # the join_input_return function runs with team_list applied to it
                    join_input_return(team_list)
                    # displays a visual showing all of the players added:
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
                    # draws every confirmation visual onto the surface
                    surface.blit(CONFIRM_TEXT, CONFIRM_RECT)
                    surface.blit(CONFIRM_1, CONFIRM_RECT1)
                    surface.blit(CONFIRM_2, CONFIRM_RECT2)
                    surface.blit(CONFIRM_3, CONFIRM_RECT3)
                    surface.blit(CONFIRM_4, CONFIRM_RECT4)
                    surface.blit(CONFIRM_5, CONFIRM_RECT5)
                    surface.blit(CONFIRM_6, CONFIRM_RECT6)
                    # empties every text box for the next team to be entered
                    text_1 = ""
                    text_2 = ""
                    text_3 = ""
                    text_4 = ""
                    text_5 = ""
                    text_6 = ""
                    # increases the team count by one, used by the host menu
                    teams += 1
                    pygame.display.update()
                    # waits 2 seconds before reverting from the confirmation view back to the normal join menu view
                    pygame.time.delay(2000)  # Delay in milliseconds
                    surface.fill(WHITE)
        
        # Defines the back button as a variable
        click_back = button(surface, 40, 650, 100, 50, "Back")
        if click_back:
            # Upon clicking the back button, calls the main menu function and returns to the main menu
            main_menu(surface, teams)
        # renders all of the input texts and input boxes
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
        # updates the display constantly
        pygame.display.update()
def join_input_return(text):
    '''Appends each team to the general list used in host_menu(), and makes a file for each of them'''
    teamX = text # sets the given team variable to "teamX"
    player_list.append(teamX) # appends the teams in "teamX" to the player_list, accessed by the host menu to retrieve all of the teams
    # creates a file named "players.csv" and appends each team to it
    fileName = folder + "/players.csv" 
    file = open(fileName,"a")    
    file.writelines(text[0] + "," + text[1] + "," + text[2] + "," + text[3] + "," + text[4] + "," + text[5])
    file.close  
# initiates pygame
pygame.init()
# initiates pygame fonts
pygame.font.init()
# declares the window aspect ratio
window_width, window_height = 1280, 720
# declares the window surface based on the window aspect ratio
window_surface = pygame.display.set_mode((window_width, window_height))
# sets the window's caption
pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
# declares folder as the command line directory location
folder = os.getcwd()
# defines all of the colours used as variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
# declares all of the fonts used as variables
font1 = pygame.font.SysFont(None, 111)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 30)
# sets "running" to true by default
running = True
# declares the initial empty text variables, used by join_menu
text_1 = ""
text_2 = ""
text_3 = ""
text_4 = ""
text_5 = ""
text_6 = ""
# declares the initial player list
player_list = []
# sets the default amount of teams to 0
teams = 0
# defines the clock
clock = pygame.time.Clock()
# for loop for if the window is closed in this state
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    mouse_state = pygame.mouse.get_pressed()
    # the initial main menu call for starting the program
    main_menu(window_surface, teams)
    pygame.display.update()
    clock.tick(60)