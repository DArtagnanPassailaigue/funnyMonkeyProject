import pygame, sys
from button import Button
    
def main_menu_screen(surface, font1, font2):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    surface.fill(WHITE)
    titleblock = font1.render("Tournament Bracket Automation", True, BLACK)
    surface.blit(titleblock, (35, 100))
    pygame.draw.rect(surface, BLACK, [0, 0, 1280, 720], 15)
    pygame.draw.rect(surface, BLACK, [0, 0, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [1230, 0, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [0, 670, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [1230, 670, 50, 50], 10)
    # Host rectangle 
    click_host = host_button(surface, font2)  # Assign the menu state returned by the function
    # Join rectangle
    click_join = join_button(surface, font2)  # Assign the menu state returned by the function
    # Quit rectangle
    click_quit = quit_button(surface, font2)
    if click_host:
        host_menu(surface, font1)
    elif click_join:
        join_menu(surface, font1)
    elif click_quit:
        pygame.quit()
        sys.exit()
        

def host_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    host_rect = pygame.Rect(400, 250, 500, 100)
    host_surface = pygame.Surface((host_rect.width, host_rect.height))
    host_surface.fill(WHITE)
    pygame.draw.rect(host_surface, BLACK, host_surface.get_rect(), 10)
    host_tourney_text = font.render("Host Tournament", True, BLACK)
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
        host_tourney_text = font.render("Host Tournament", True, BLACK)
        host_text_centre = host_tourney_text.get_rect(center=host_surface.get_rect().center)
        host_surface.blit(host_tourney_text, host_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True

    surface.blit(host_surface, host_rect)
    return click
    
def join_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    join_rect = pygame.Rect(400, 400, 500, 100)
    join_surface = pygame.Surface((join_rect.width, join_rect.height))
    join_surface.fill(WHITE)
    pygame.draw.rect(join_surface, BLACK, join_surface.get_rect(), 10)
    join_tourney_text = font.render("Join Tournament", True, BLACK)
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
        join_tourney_text = font.render("Join Tournament", True, BLACK)
        join_text_centre = join_tourney_text.get_rect(center=join_surface.get_rect().center)
        join_surface.blit(join_tourney_text, join_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
        
    surface.blit(join_surface, join_rect)
    return click


def quit_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    quit_rect = pygame.Rect(530, 550, 250, 75)
    quit_surface = pygame.Surface((quit_rect.width, quit_rect.height))
    quit_surface.fill(WHITE)
    pygame.draw.rect(quit_surface, BLACK, quit_surface.get_rect(), 10)
    quit_tourney_text = font.render("Quit", True, BLACK)
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
        quit_tourney_text = font.render("Quit", True, BLACK)
        quit_text_centre = quit_tourney_text.get_rect(center=quit_surface.get_rect().center)
        quit_surface.blit(quit_tourney_text, quit_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True
        
    surface.blit(quit_surface,  quit_rect)
    return click

def back_menu_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    click = False
    back_rect = pygame.Rect(1000, 600, 100, 50)
    back_surface = pygame.Surface((back_rect.width, back_rect.height))
    back_surface.fill(WHITE)
    pygame.draw.rect(back_surface, BLACK, back_surface.get_rect(), 10)
    back_tourney_text = font.render("Back", True, BLACK)
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
        back_tourney_text = font.render("Back", True, BLACK)
        back_text_centre = back_tourney_text.get_rect(center=back_surface.get_rect().center)
        back_surface.blit(back_tourney_text, back_text_centre)
        if pygame.mouse.get_pressed()[0]:
            click = True

    surface.blit(back_surface, back_rect)
    return click

def host_menu(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    while True:

        surface.fill(WHITE)

        PLAY_TEXT = font.render("Host Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        surface.blit(PLAY_TEXT, PLAY_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        click_back = back_menu_button(surface, font)
        if click_back:
            main_menu_screen(surface, font, font1)

        pygame.display.update()
        
def join_menu(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    while True:

        surface.fill(WHITE)

        PLAY_TEXT = font.render("Join Menu", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        surface.blit(PLAY_TEXT, PLAY_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    
pygame.init()
pygame.font.init()
window_width, window_height = 1280, 720
window_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
font1 = pygame.font.SysFont(None, 111)
font2 = pygame.font.SysFont(None, 50)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    mouse_state = pygame.mouse.get_pressed()
    main_menu_screen(window_surface, font1, font2)
    pygame.display.update()
    clock.tick(60)

