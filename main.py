import pygame
import sys

def mainmenu():
    pygame.init()
    pygame.font.init()
    window_width, window_height = 1536, 864
    window_surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    menu_state = "main_menu"
    font1 = pygame.font.SysFont(None, 135)
    font2 = pygame.font.SysFont(None, 50)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        mouse_state = pygame.mouse.get_pressed()
        if menu_state == "main_menu":
            window_surface.fill((255, 255, 255))  # Clear the screen
            menu_state = main_menu_screen(window_surface, font1, font2, mouse_state)
        elif menu_state == "host_menu":
            host_menu(window_surface, font1)
            return "host_menu"  # Add this line to return the menu state
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    
def main_menu_screen(surface, font1, font2, mouse):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    surface.fill(WHITE)
    titleblock = font1.render("Tournament Bracket Automation", True, BLACK)
    surface.blit(titleblock, (35, 100))
    pygame.draw.rect(surface, BLACK, [0, 0, 1536, 864], 15)
    pygame.draw.rect(surface, BLACK, [0, 0, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [1486, 0, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [0, 814, 50, 50], 10)
    pygame.draw.rect(surface, BLACK, [1486, 814, 50, 50], 10)
    # Host rectangle 
    menu_state = host_button(surface, font2, mouse)  # Assign the menu state returned by the function
    if menu_state is not None:  # Check if the menu state is not None
        return menu_state
    # Join rectangle
    menu_state = join_button(surface, font2, mouse)  # Assign the menu state returned by the function
    if menu_state is not None:  # Check if the menu state is not None
        return menu_state

def host_button(surface, font, mouse):
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
        if mouse[0] == 1:  # Check if the left mouse button was pressed down
            return "host_menu"  # Return the menu state

    surface.blit(host_surface, host_rect)
    return None

    
def join_button(surface, font, mouse):
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
        if mouse[0] == 1:  # Check if the left mouse button was pressed down
            return "join_menu"  # Return the menu state
        
    surface.blit(join_surface, join_rect)
    return None
        
def host_menu(surface, font):
    # Implement the host menu here
    # This is just a placeholder for demonstration
    surface.fill((255, 0, 0))  # Fill the screen with red color
    text = font.render("Host Menu", True, (255, 255, 255))
    text_rect = text.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
    surface.blit(text, text_rect)
    
# Call the mainmenu function
mainmenu()

