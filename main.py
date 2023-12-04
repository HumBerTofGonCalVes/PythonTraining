import pygame, sys, random
from pygame.math import Vector2

#Fixed variables
CELL_SIZE= 40
CELL_NUMBER_WIDTH = 20
CELL_NUMBER_HEIGHT = 20
FRAMERATE = 60

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        
    def draw_snake(self):
        for block in self.body:
            # Create a rectangle
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            #Draw the rectangle
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)

class FRUIT:
    def __init__(self):
        # Create an x and y position
        self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        self.pos = Vector2(self.x, self.y)
        
    # Draw a square
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER_WIDTH, CELL_SIZE * CELL_NUMBER_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

#test_surface = pygame.Surface((100,200))
#test_surface.fill((0,0,255))
#x_pos = 200
#test_rect = pygame.Rect(100, 200, 100, 100)   # Rectangle allows me to have a different control than the surface! Less code
#test_rect = test_surface.get_rect(center = (200, 250))      # Gets the surface and puts a rectangle around it

while True:
    
    # Search for events
    for event in pygame.event.get():
        
        # Search for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw all our elements
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    #test_rect.right += 1
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #x_pos -= 1
    #screen.blit(test_surface, (x_pos, 250))
    #screen.blit(test_surface, test_rect)   # blit -> block image transfer      //      position is in the top left corner of the surface
    
    pygame.display.update()
    clock.tick(FRAMERATE)