import itertools
import pygame, sys, random
from pygame.math import Vector2

# Constants
CELL_SIZE= 40
CELL_NUMBER_WIDTH = 25
CELL_NUMBER_HEIGHT = 20
FRAMERATE = 60

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        
        # Import snake images
        self.head_up = pygame.image.load('src/files/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('src/files/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('src/files/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('src/files/Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('src/files/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('src/files/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('src/files/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('src/files/Graphics/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('src/files/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('src/files/Graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('src/files/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('src/files/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('src/files/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('src/files/Graphics/body_bl.png').convert_alpha()
        
        # Import sound
        self.crunch_sound = pygame.mixer.Sound('src/files/Sound/crunch.wav')
        
    def draw_snake(self):  # sourcery skip: low-code-quality
        #for block in self.body:
            # Create a rectangle
            #snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            #Draw the rectangle
            #pygame.draw.rect(screen, (183, 111, 122), snake_rect)
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # Rect for the positioning
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            # What direction is facing
            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, snake_rect)
                elif previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    screen.blit(self.body_tl, snake_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    screen.blit(self.body_bl, snake_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    screen.blit(self.body_tr, snake_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    screen.blit(self.body_br, snake_rect)
            #else:
                #pygame.draw.rect(screen, (150, 100, 100), snake_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        if head_relation == Vector2(0, 1): self.head = self.head_up
        if head_relation == Vector2(0, -1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        if tail_relation == Vector2(0, 1): self.tail = self.tail_up
        if tail_relation == Vector2(0, -1): self.tail = self.tail_down
    
    def move_snake(self):
        body_copy = self.body[:] if self.new_block == True else self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False
        
    def add_block(self):
        self.new_block = True

    def play_sound_crunch(self):
        self.crunch_sound.play()

class FRUIT:
    def __init__(self):
        # Create an x and y position
        #self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        #self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        #self.pos = Vector2(self.x, self.y)
        self.apple = pygame.image.load('src/files/Graphics/apple.png').convert_alpha()
        self.randomize()
        
    # Draw a square
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(self.apple, fruit_rect)
    
    def randomize(self):
        # Create an arbitrary x and y position
        self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.game_font = pygame.font.Font('src/files/Font/PoetsenOne-Regular.ttf', 25)
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # Reposition the fruit
            self.fruit.randomize()
            # Add another block to the snake
            self.snake.add_block()
            # Play crunch sound
            self.snake.play_sound_crunch()
            
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
        
    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row, col in itertools.product(range(CELL_NUMBER_HEIGHT), range(CELL_NUMBER_WIDTH)):
            if row % 2 == 0 and col % 2 == 0 or row % 2 != 0 and col % 2 != 0:
                grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER_WIDTH - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER_HEIGHT - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,apple_rect.height)
        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)  # Designs a frae around it
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.apple, apple_rect)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER_WIDTH, CELL_SIZE * CELL_NUMBER_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()


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
            if event.key == pygame.K_LEFT and  main_game.snake.direction.x != 1:
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