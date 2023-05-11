import pygame

class Bee:

    def __init__(self):

        self.x = 0
        self.y = 405
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def liiku(self):
        if self.right:
            self.x += 2
        if self.left:
            self.x -= 2
        if self.up:
            self.y -= 2
        if self.down:
            self.y += 2

	#pidetään hahmo sisällä

        if self.x <= 0:
            self.left = False
        if self.x >= 570:
            self.right = False
        if self.y <= 0:
            self.up = False
        if self.y >= 405:
            self.down = False

