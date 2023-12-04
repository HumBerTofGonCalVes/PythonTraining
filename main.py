import pygame, sys

#Fixed variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
FRAMERATE = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()

while True:
    # Search for events
    for event in pygame.event.get():
        # Search for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Draw all our elements
    pygame.display.update()
    clock.tick(FRAMERATE)