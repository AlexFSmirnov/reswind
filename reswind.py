import pygame
from pygame import *


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
        
        self.main_size = main_size
        self.current_size = initial_size
        
        self.draw_lines = draw_lines
        self.lines_color = lines_color
        
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
        
    def updateMainSurface(self, new_main_surface):
        self.main_surface = pygame.transform.scale(new_main_surface, 
                                                   main_size)
        
    def updateBackgroundSurface(self):
        self.background_surface.fill((0, 0, 0))
        d_h, d_w = self.display_surface.get_size()
        m_w, m_h = self.main_size
        gap = self.gap_fill
        
        # Now we need to check, whether the gaps are above and
        # below the main surface or on it's sides.
        if d_h / (d_w / m_w) >= m_h:  # If they are above and below.
            gap_size = (d_w, round((d_h - d_w / m_w * m_h) / 2))
            gap_top = transform.scale(transform.rotate(gap, 180), gap_size)
            gap_bottom = transform.scale(transform.rotate(gap, 0), gap_size)
            
            self.background_surface.blit(gap_top, (0, 0))
            self.background_surface.blit(gap_bottom, (0, d_h - gap_size[1]))
            
            if self.draw_lines:
                # -1 here - sort of a duct tape. It works, and idk why :P
                draw.line(self.background_surface, self.lines_color,
                          (0, gap_size[1] - 1), (d_w, gap_size[1] - 1), 6)
                draw.line(self.background_surface, self.lines_color,
                                  (0, d_h - gap_size[1] - 1), 
                                  (d_w, d_h - gap_size[1] - 1), 6)                 
    
    def update(self):
            pass
        


pygame.init()

screen = pygame.display.set_mode((300, 300))
screen.fill((255,255,255))

while True:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        pygame.quit()
    
    if e.type == pygame.KEYDOWN and e.key == pygame.K_q:
        a = ResizableWindow((300, 300), (300, 250), 
                            gap_fill_type="gradient_up", 
                            gap_fill_color=(0, 100, 0))
        a.updateBackgroundSurface()
        screen.blit(a.background_surface, (0, 0))
        
    if e.type == KEYDOWN and e.key == K_w: 
        draw.rect(screen, (255,255,255), (0, 25, 300, 250))
        
        
    pygame.display.update()