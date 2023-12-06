from src.models.classes.snake import SNAKE
from src.models.classes.fruit import FRUIT
import pygame, itertools
from src.models.constants.game_constants import CELL_NUMBER_WIDTH, CELL_NUMBER_HEIGHT, CELL_SIZE

class MAIN:
    def __init__(self, screen):
        self.screen = screen
        self.snake = SNAKE(self.screen)
        self.fruit = FRUIT(self.screen)
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
            
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            
    def check_fail(self):
        # Check if snake is outside the screen
        if not 0 <= self.snake.body[0].x < CELL_NUMBER_WIDTH or not 0 <= self.snake.body[0].y < CELL_NUMBER_HEIGHT:
            self.game_over()
        # Check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        self.snake.reset()
        
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row, col in itertools.product(range(CELL_NUMBER_HEIGHT), range(CELL_NUMBER_WIDTH)):
            if row % 2 == 0 and col % 2 == 0 or row % 2 != 0 and col % 2 != 0:
                grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER_WIDTH - 60)
        score_y = int(CELL_SIZE * CELL_NUMBER_HEIGHT - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,apple_rect.height)
        pygame.draw.rect(self.screen, (167, 209, 61), bg_rect)
        pygame.draw.rect(self.screen, (56, 74, 12), bg_rect, 2)  # Designs a frae around it
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.fruit.apple, apple_rect)