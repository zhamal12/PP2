import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


ball = Ball(250, 250, 25, 20, WIDTH, HEIGHT)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move_left()

            if event.key == pygame.K_RIGHT:
                ball.move_right()

            if event.key == pygame.K_UP:
                ball.move_up()

            if event.key == pygame.K_DOWN:
                ball.move_down()

    screen.fill((255, 255, 255))

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


