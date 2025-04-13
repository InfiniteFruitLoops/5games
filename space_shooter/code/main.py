#When you've written more stuff, it's a good idea to put a header here explaining what things do
import pygame #It is always a good idea to check that your imports work!
pygame.init() #Always initialise the module
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 620 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
running = True

while running:
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    #Draw loop