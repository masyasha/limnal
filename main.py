import sys, pygame
pygame.init()

size = width, height = 400, 700
speed = 10
black = 255, 255, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball = pygame.image.load("tot2.png")
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()
ballrect.x = int(width/2)

face_direction = 'right'

def dispatch_press(e, false=None):
    if e.key == pygame.K_LEFT and false != 'l':
        return (-speed, 1)
    if e.key == pygame.K_RIGHT and false != 'r':
        return (speed, 1)
    return (0, 1)

while 1:
    move = (0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if ballrect.left < 0:
                move = dispatch_press(event, 'l')
            elif ballrect.right > width:
                move = dispatch_press(event, 'r')
            else:
                move = dispatch_press(event)
    if move[0] > 0 and face_direction != 'right':
        ball = pygame.transform.flip(ball, True, False)
        face_direction = 'right'
    if move[0] < 0 and face_direction != 'left':
        ball = pygame.transform.flip(ball, True, False)
        face_direction = 'left'

    ballrect = ballrect.move(move)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(40)
