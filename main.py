import sys, pygame
import player

size = width, height = 400, 700
speed = 10
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

    while 1:
        move = [0, 1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # !!!!!!!!!!
        if move[0] > 0 and face_direction != 'right':
            face_direction = 'right'
        if move[0] < 0 and face_direction != 'left':
            face_direction = 'left'

        screen.blit(bg, (0, 0))
        objects.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
