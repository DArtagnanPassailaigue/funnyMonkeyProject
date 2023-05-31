import pygame

def mainmenu():
    pygame.init()
    pygame.font.init()
    window_width, window_height = 1536, 864
    window_surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font1 = pygame.font.SysFont(None, 135)
    font2 = pygame.font.SysFont(None, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window_surface.fill(WHITE)
        titleblock = font1.render("Tournament Bracket Automation", True, BLACK)
        window_surface.blit(titleblock, (35, 100))
        pygame.draw.rect(window_surface, BLACK, [0, 0, 1536, 864], 15)
        pygame.draw.rect(window_surface, BLACK, [0, 0, 50, 50], 10)
        pygame.draw.rect(window_surface, BLACK, [1486, 0, 50, 50], 10)
        pygame.draw.rect(window_surface, BLACK, [0, 814, 50, 50], 10)
        pygame.draw.rect(window_surface, BLACK, [1486, 814, 50, 50], 10)
        # Host rectangle 
        host_button(window_surface, font2) 
        # Join rectangle
        join_button(window_surface, font2)
        pygame.display.update()
    pygame.quit()

def host_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    host_rect = pygame.Rect(500, 250, 500, 100)
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
        
    surface.blit(host_surface, host_rect)
    
def join_button(surface, font):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (180, 180, 180)
    join_rect = pygame.Rect(500, 400, 500, 100)
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
        
    surface.blit(join_surface, join_rect)
        
# Call the mainmenu function
mainmenu()
