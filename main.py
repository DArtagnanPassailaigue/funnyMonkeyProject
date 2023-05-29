import pygame

def mainmenu():
    pygame.init()
    pygame.font.init()
    window_width, window_height = 1536, 864
    window_surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tournament Bracket Automation (T.B.A.) - Sponsored by Fortnite")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 135)
    #text_box_rect = pygame.Rect(700, 200, 300, 100)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window_surface.fill(WHITE)
        #pygame.draw.rect(window_surface, BLACK, text_box_rect, 2)
        text_surface = font.render("Tournament Bracket Automation", True, BLACK)
        window_surface.blit(text_surface, (35, 100))
        
        pygame.display.update()
    
    pygame.quit()

# Call the mainmenu function
mainmenu()
