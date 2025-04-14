#When you've written more stuff, it's a good idea to put a header here explaining what things do
import pygame #It is always a good idea to check that your imports work!
from os.path import join #To ensure path not OS dependent

pygame.init() #Always initialise the module
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 620 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

running = True

#Importing an image   
player_surf = pygame.image.load(join('..','images','player.png')).convert_alpha() #To ensure robustness
x = 100
while running:
    x += 0.1
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    #Draw loop
    display_surface.fill('darkgray')
    display_surface.blit(player_surf,(x,100))
    pygame.display.update()

pygame.quit() 