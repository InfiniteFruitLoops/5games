#When you've written more stuff, it's a good idea to put a header here explaining what things do

#It is always a good idea to check that your imports work!
import pygame
from os.path import join #To ensure path not OS dependent
from random import randint #For star placement

#General purpose Initialisation
pygame.init() #Always initialise the module
clock = pygame.time.Clock()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 620 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

#Import player   
player_surf = pygame.image.load(join('..','images','player.png')).convert_alpha() #To ensure robustness
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
PLAYER_SPEED = 0.4
player_direction = +1

#Import star
star_surf = pygame.image.load(join('..','images','star.png')).convert_alpha()
#Initialise  list of 20 random star positions
star_pos = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

#Import meteor
meteor_surf = pygame.image.load(join('..','images','meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

#Import laser
laser_surf = pygame.image.load(join('..','images','laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))


while running:
    clock.tick(60)
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

    #Draw meteor
    display_surface.blit(meteor_surf, meteor_rect)

    #Draw laser
    display_surface.blit(laser_surf, laser_rect)

    #Draw and move player
    display_surface.blit(player_surf,player_rect)
    player_rect.left += player_direction * PLAYER_SPEED
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction = player_direction * -1
    
    pygame.display.update()

pygame.quit() 