import pygame
from pygame import *
import reswind
import sys


pygame.init()
window = reswind.ResizableWindow((300, 300), (300, 300),
                                 gap_fill_type  = "gradient_up",
                                 gap_fill_color = (0, 0, 0),
                                 gap_steps      = 100,
                                 draw_lines     = True,
                                 lines_color    = (100, 100, 100),
                                 smoothscale    = False)

window.main_surface.fill((0, 255, 0))
draw.circle(window.main_surface, (0, 0, 0), (150, 150), 100)

while True:   
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    
    if e.type == VIDEORESIZE:
        window.updateSize(e.dict['size'])        
    
    window.update()
    