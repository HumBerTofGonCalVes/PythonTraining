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
        self.direction = Vector2(1, 0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            # Create a rectangle
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            #Draw the rectangle
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)
    
    def move_snake(self):
        body_copy = self.body[:] if self.new_block == True else self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False
        
    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        # Create an x and y position
        #self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        #self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        #self.pos = Vector2(self.x, self.y)
        self.randomize()
        
    # Draw a square
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)
    
    def randomize(self):
        # Create an arbitrary x and y position
        self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # Reposition the fruit
            self.fruit.randomize()
            # Add another block to the snake
            self.snake.add_block()
            
    def check_fail(self):
        # Check if snake is outside the screen
        if not 0 <= self.snake.body[0].x < CELL_NUMBER_WIDTH or not 0 <= self.snake.body[0].y < CELL_NUMBER_HEIGHT:
            self.game_over()
        # Check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER_WIDTH, CELL_SIZE * CELL_NUMBER_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

#fruit = FRUIT()
#snake = SNAKE()

#test_surface = pygame.Surface((100,200))
#test_surface.fill((0,0,255))
#x_pos = 200
#test_rect = pygame.Rect(100, 200, 100, 100)   # Rectangle allows me to have a different control than the surface! Less code
#test_rect = test_surface.get_rect(center = (200, 250))      # Gets the surface and puts a rectangle around it

SCREEN_UPDATE = pygame.USEREVENT        # Timer for our snake (without user interaction)
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    
    # Search for events
    for event in pygame.event.get():
        
        # Search for quit event
        if event.type == pygame.QUIT:
            #pygame.quit()
            #sys.exit()
            main_game.game_over()
        if event.type == SCREEN_UPDATE:
            #snake.move_snake()
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and  main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(-1, 0)

    # Draw all our elements
    screen.fill((175, 215, 70))
    #fruit.draw_fruit()
    #snake.draw_snake()
    
    #test_rect.right += 1
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #x_pos -= 1
    #screen.blit(test_surface, (x_pos, 250))
    #screen.blit(test_surface, test_rect)   # blit -> block image transfer      //      position is in the top left corner of the surface
    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FRAMERATE)