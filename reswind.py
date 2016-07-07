import pygame


class ResizableWindow:
    def __init__(self,
                 initial_size,
                 main_size,
                 gap_fill_type  = "solid_color",
                 gap_fill_color = (0, 0, 0),
                 draw_lines     = True,
                 lines_color    = (100, 100, 100)):
        
        self.display_surface    = pygame.Surface(initial_size)
        self.background_surface = pygame.Surface(initial_size)
        self.main_surface       = pygame.Surface(main_size)
        
        # Creating the gap fill.  
        self.gap_fill = pygame.Surface((100, 100))
        if gap_fill_type == "solid_color":
            self.gap_fill.fill(gap_fill_color)
        elif gap_fill_type == "gradient_up":
            for y in range(100):
                for x in range(100):
                    self.gap_fill.set_at((x, y), gap_fill_color)
                gap_fill_color = [min(i + 1, 255) for i in gap_fill_color]
        elif gap_fill_type == "gradient_down":
            for y in range(100):
                for x in range(100):
                    self.gap_fill.set_at((x, y), gap_fill_color)
                gap_fill_color = [max(i - 1, 0) for i in gap_fill_color]        


pygame.init()

screen = pygame.display.set_mode((300, 300))
screen.fill((255,255,255))

while True:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        pygame.quit()
    
    if e.type == pygame.KEYDOWN and e.key == pygame.K_q:
        a = ResizableWindow((100, 100), (100, 100), 
                            gap_fill_type="gradient_down", 
                            gap_fill_color=(255, 45, 0))
        screen.blit(a.gap_fill, (20, 20))
        
        
    pygame.display.update()