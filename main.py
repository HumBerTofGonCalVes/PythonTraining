import pygame, sys
from pygame.math import Vector2
from src.models.classes import MAIN
from src.models.constants.game_constants import CELL_NUMBER_WIDTH, CELL_NUMBER_HEIGHT, CELL_SIZE, FRAMERATE

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER_WIDTH, CELL_SIZE * CELL_NUMBER_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT        # Timer for our snake (without user interaction)
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN(screen)

while True:
    
    # Search for events
    for event in pygame.event.get():
        # Search for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(FRAMERATE)