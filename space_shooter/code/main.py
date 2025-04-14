#When you've written more stuff, it's a good idea to put a header here explaining what things do

#It is always a good idea to check that your imports work!
import pygame
from os.path import join #To ensure path not OS dependent
from random import randint #For star placement

pygame.init() #Always initialise the module
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 620 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

running = True

#Import player   
player_surf = pygame.image.load(join('..','images','player.png')).convert_alpha() #To ensure robustness
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

#Import star
star_surf = pygame.image.load(join('..','images','star.png')).convert_alpha()
#Initialise  list of 20 random star positions
star_pos = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]

while running:
    #Event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
 
    #Draw loop

    #Fill surface
    display_surface.fill('darkgray')
    
    #Randomly position and draw stars
    for i in range(20):
        display_surface.blit(star_surf,star_pos[i])

    #Draw and move player
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 0.2
    display_surface.blit(player_surf,player_rect)
    
    pygame.display.update()

pygame.quit() 