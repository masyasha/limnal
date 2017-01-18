import pygame
from pygame import *
import main

color = "#1442e7"  # idk
width = 50
height = 35


class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.x = int(main.width/2)
        self.y = main.height
        self.x_vel = self.y_vel = 0
        self.image = Surface((width, height))
        self.image.fill(Color(color))
        self.rect = Rect(self.x, self.y, width, height)
        print("rendered")
