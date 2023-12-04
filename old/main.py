import pygame, sys, random
from pygame.math import Vector2

CELL_SIZE = 40
CELL_NUMBER = 20
BOARD_WIDTH = BOARD_HEIGHT = CELL_SIZE * CELL_NUMBER
FRAMERATE = 60

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            # Create a rectangle to draw
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            # Draw the rect
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)
            
    def move_snake(self):  # sourcery skip: hoist-statement-from-if
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block == False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        #Create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        #Draw the rectangle
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen, (126, 166, 114),fruit_rect)
        
    def randomize(self):
        #Create an x and y position
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
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
        # Check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
        # Check if the snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    # draw all our elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, +1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(+1, 0)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
    
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FRAMERATE)