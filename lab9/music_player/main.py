import pygame
import sys
from player import Player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

player = Player("music")
player.play()

running = True

while running:
    screen.fill((20, 20, 20))

    text = font.render(f"Track: {player.get_track_name()}", True, (255, 255, 255))
    screen.blit(text, (20, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                if player.playing:
                    player.pause()
                else:
                    player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.prev()

            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()