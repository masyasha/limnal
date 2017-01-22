from pygame import *
import main

color = "#14f74e"  # idk
width, height = 30, 45
speed = 10


class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.x = int(main.width/2)
        self.y = int(main.height - height)
        self.x_vel = self.y_vel = 0
        self.image = Surface((width, height))
        self.image.fill(Color(color))
        self.rect = Rect(self.x, self.y, width, height)

    def update(self, up, right, left):
        if up:
            self.y_vel = -speed

        if right:
            self.x_vel = speed

        if left:
            self.x_vel = -speed

        if not up:
            self.y_vel = 0
        if not (left or right):
            self.x_vel = 0

        self.rect.y += self.y_vel
        self.rect.x += self.x_vel

    def draw(self, screen):
        draw.rect(screen, Color(color), self.rect)
