import pygame, sys
from button import Button
    
def main_menu_screen(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
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
        click_host = host_button(surface)  # Assign the menu state returned by the function
        # Join rectangle
        click_join = join_button(surface)  # Assign the menu state returned by the function
        # Quit rectangle
        click_quit = quit_button(surface)
        if click_host:
            host_menu(surface)
        elif click_join:
            join_menu(surface, "")
        elif click_quit:
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
        

def host_button(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    host_rect = pygame.Rect(400, 250, 500, 100)
    host_surface = pygame.Surface((host_rect.width, host_rect.height))
    host_surface.fill(WHITE)
    pygame.draw.rect(host_surface, BLACK, host_surface.get_rect(), 10)
    host_tourney_text = font2.render("Host Tournament", True, BLACK)
    host_text_centre = host_tourney_text.get_rect(center=host_surface.get_rect().center)
    host_surface.blit(host_tourney_text, host_text_centre)

    mouse_pos = pygame.mouse.get_pos()
    if host_rect.collidepoint(mouse_pos):
        host_hovering = True
    else:
        host_hovering = False

    if host_hovering:
        host_surface.fill(GREY)
        pygame.draw.rect(host_surface, BLACK, host_surface.get_rect(), 10)
        host_tourney_text = font2.render("Host Tournament", True, BLACK)
        host_text_centre = host_tourney_text.get_rect(center=host_surface.get_rect().center)
        host_surface.blit(host_tourney_text, host_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True

    surface.blit(host_surface, host_rect)
    return click
    
def join_button(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    join_rect = pygame.Rect(400, 400, 500, 100)
    join_surface = pygame.Surface((join_rect.width, join_rect.height))
    join_surface.fill(WHITE)
    pygame.draw.rect(join_surface, BLACK, join_surface.get_rect(), 10)
    join_tourney_text = font2.render("Join Tournament", True, BLACK)
    join_text_centre = join_tourney_text.get_rect(center=join_surface.get_rect().center)
    join_surface.blit(join_tourney_text, join_text_centre)
        
    mouse_pos = pygame.mouse.get_pos()
    if join_rect.collidepoint(mouse_pos):
        join_hovering = True
    else:
        join_hovering = False
        
    if join_hovering:
        join_surface.fill(GREY)
        pygame.draw.rect(join_surface, BLACK, join_surface.get_rect(), 10)
        join_tourney_text = font2.render("Join Tournament", True, BLACK)
        join_text_centre = join_tourney_text.get_rect(center=join_surface.get_rect().center)
        join_surface.blit(join_tourney_text, join_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
        
    surface.blit(join_surface, join_rect)
    return click


def quit_button(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    quit_rect = pygame.Rect(530, 550, 250, 75)
    quit_surface = pygame.Surface((quit_rect.width, quit_rect.height))
    quit_surface.fill(WHITE)
    pygame.draw.rect(quit_surface, BLACK, quit_surface.get_rect(), 10)
    quit_tourney_text = font2.render("Quit", True, BLACK)
    quit_text_centre = quit_tourney_text.get_rect(center=quit_surface.get_rect().center)
    quit_surface.blit(quit_tourney_text, quit_text_centre)
        
    mouse_pos = pygame.mouse.get_pos()
    if quit_rect.collidepoint(mouse_pos):
        quit_hovering = True
    else:
        quit_hovering = False
        
    if quit_hovering:
        quit_surface.fill(GREY)
        pygame.draw.rect(quit_surface, BLACK, quit_surface.get_rect(), 10)
        quit_tourney_text = font2.render("Quit", True, BLACK)
        quit_text_centre = quit_tourney_text.get_rect(center=quit_surface.get_rect().center)
        quit_surface.blit(quit_tourney_text, quit_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
        
    surface.blit(quit_surface,  quit_rect)
    return click

def back_menu_button(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    back_rect = pygame.Rect(40, 650, 100, 50)
    back_surface = pygame.Surface((back_rect.width, back_rect.height))
    back_surface.fill(WHITE)
    pygame.draw.rect(back_surface, BLACK, back_surface.get_rect(), 10)
    back_tourney_text = font3.render("Back", True, BLACK)
    back_text_centre = back_tourney_text.get_rect(center=back_surface.get_rect().center)
    back_surface.blit(back_tourney_text, back_text_centre)

    mouse_pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(mouse_pos):
        back_hovering = True
    else:
        back_hovering = False

    if back_hovering:
        back_surface.fill(GREY)
        pygame.draw.rect(back_surface, BLACK, back_surface.get_rect(), 10)
        back_tourney_text = font3.render("Back", True, BLACK)
        back_text_centre = back_tourney_text.get_rect(center=back_surface.get_rect().center)
        back_surface.blit(back_tourney_text, back_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True

    surface.blit(back_surface, back_rect)
    return click

def host_menu(surface):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    while True:

        surface.fill(WHITE)

        PLAY_TEXT = font1.render("Host Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        surface.blit(PLAY_TEXT, PLAY_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        click_back = back_menu_button(surface)
        if click_back:
            main_menu_screen(surface)

        pygame.display.update()    
        
def join_menu(surface, text):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    text_editing = False
    text_rect_height = 325
    boxnum = 0

    while True:
        surface.fill(WHITE)
        PLAY_TEXT = font1.render("Join Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        surface.blit(PLAY_TEXT, PLAY_RECT)

        text_rect = pygame.Rect(400, text_rect_height, 500, 50)
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
                    CONFIRM_TEXT = font3.render("Player " + text + " added.", True, BLACK)
                    CONFIRM_RECT = CONFIRM_TEXT.get_rect(center=(640, 700))
                    surface.blit(CONFIRM_TEXT, CONFIRM_RECT)
                    pygame.display.update()
                    pygame.time.delay(2000)  # Delay in milliseconds
                    surface.fill(WHITE)
                    #upon revamping the button functions, add a back button and add player button here

        click_back = back_menu_button(surface)
        click_add = addplayer_button(surface)
        if click_back:
            main_menu_screen(surface)
        elif click_add:
            text_rect_height += 25
            boxnum += 1
            addplayer(surface, text_rect_height, boxnum)

        input_text = font2.render(text, True, BLACK)
        input_rect = input_text.get_rect(center=text_rect.center)
        surface.blit(text_surface, text_rect)
        surface.blit(input_text, input_rect)

        pygame.display.update()

def addplayer_button(surface):
    click = False
    add_rect = pygame.Rect(500, 200, 300, 75)
    add_surface = pygame.Surface((add_rect.width, add_rect.height))
    add_surface.fill(WHITE)
    pygame.draw.rect(add_surface, BLACK, add_surface.get_rect(), 10)
    add_tourney_text = font2.render("+ Add Teammate", True, BLACK)
    add_text_centre = add_tourney_text.get_rect(center=add_surface.get_rect().center)
    add_surface.blit(add_tourney_text, add_text_centre)

    mouse_pos = pygame.mouse.get_pos()
    if add_rect.collidepoint(mouse_pos):
        add_hovering = True
    else:
        add_hovering = False

    if add_hovering:
        add_surface.fill(GREY)
        pygame.draw.rect(add_surface, BLACK, add_surface.get_rect(), 10)
        add_tourney_text = font2.render("+ Add Teammate", True, BLACK)
        add_text_centre = add_tourney_text.get_rect(center=add_surface.get_rect().center)
        add_surface.blit(add_tourney_text, add_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True

    surface.blit(add_surface, add_rect)


def addplayer(surface, height, box_num):
    # come back to this later
    pass
    '''
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    extra_boxes = []
    while True:
        box_num
    '''
            
        
def join_input_return(text):
    playerX = text
    print(playerX)
    # ruban's player input code will go here

pygame.init()
pygame.font.init()
window_width, window_height = 1280, 720
window_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
font1 = pygame.font.SysFont(None, 111)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 30)
running = True
text = ""
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    mouse_state = pygame.mouse.get_pressed()
    main_menu_screen(window_surface)
    pygame.display.update()
    clock.tick(60)