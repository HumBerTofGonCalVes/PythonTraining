import pygame, random
from pygame.math import Vector2
from ..constants.game_constants import CELL_NUMBER_WIDTH, CELL_NUMBER_HEIGHT, CELL_SIZE

class FRUIT:
    def __init__(self, screen):
        self.screen = screen
        self.apple = pygame.image.load('src/files/Graphics/apple.png').convert_alpha()
        self.randomize()
        
    # Draw a square
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.screen.blit(self.apple, fruit_rect)
    
    def randomize(self):
        # Create an arbitrary x and y position
        self.x = random.randint(0, CELL_NUMBER_WIDTH-1)
        self.y = random.randint(0, CELL_NUMBER_HEIGHT-1)
        self.pos = Vector2(self.x, self.y)