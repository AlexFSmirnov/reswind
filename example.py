import pygame
from pygame import *
import reswind


pygame.init()


window = reswind.ResizableWindow((300, 300), (300, 300),
                         gap_fill_type="gradient_down",
                         gap_fill_color=(0, 255, 0),
                         gap_steps=100,
                         draw_lines=False)

window.main_surface.fill((0,255,0))

while True:   
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        pygame.quit()
    
    if e.type == VIDEORESIZE:
        window.updateSize(e.dict['size'])
        
    if e.type == KEYDOWN and e.key == K_w: 
        print(pygame.display.Info())
        
    
    window.update()
    