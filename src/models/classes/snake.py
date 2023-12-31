from pygame.math import Vector2
import pygame
from src.models.constants.game_constants import CELL_SIZE

class SNAKE:
    def __init__(self, screen):
        self.screen = screen
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
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
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # Rect for the positioning
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            # What direction is facing
            if index == 0:
                self.screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                self.screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.screen.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    self.screen.blit(self.body_horizontal, snake_rect)
                elif previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    self.screen.blit(self.body_tl, snake_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    self.screen.blit(self.body_bl, snake_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    self.screen.blit(self.body_tr, snake_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    self.screen.blit(self.body_br, snake_rect)
    
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

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
