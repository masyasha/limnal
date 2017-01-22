import pygame
import player
from pygame import *

size = width, height = 900, 650
color = "#ff7f7f"


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    bg = pygame.Surface(size)
    bg.fill(pygame.Color(color))
    clock = pygame.time.Clock()
    skier = player.Player()

    face_direction = 'right'

    right = left = up = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: exit()
            if e.type == KEYDOWN:
                if e.key == K_UP: up = True
                if e.key == K_RIGHT: right = True
                if e.key == K_LEFT: left = True
            if e.type == KEYUP:
                if e.key == K_UP: up = False
                if e.key == K_RIGHT: right = False
                if e.key == K_LEFT: left = False

        screen.blit(bg, (0, 0))
        skier.update(up, right, left)
        skier.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
