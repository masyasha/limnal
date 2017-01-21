import sys, pygame
import player
from pygame import *

size = width, height = 400, 700
color = "#ff7f7f"


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    bg = pygame.Surface(size)
    bg.fill(pygame.Color(color))
    clock = pygame.time.Clock()
    skier = player.Player()
    objects = pygame.sprite.Group()
    objects.add(skier)

    face_direction = 'right'

    down = up = False
    right = left = False

    hotKeysDown = {274: lambda x: skier.update(x, up, left, right),      # down key
                   273: lambda x: skier.update(down, x, left, right),        # up key
                   276: lambda x: skier.update(down, up, x, right),      # left key
                   275: lambda x: skier.update(down, up, left, x)}     # right key

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == KEYDOWN:
                hotKeysDown[e.key](True)
#            if e.type == KEYUP:

        screen.blit(bg, (0, 0))
        objects.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
