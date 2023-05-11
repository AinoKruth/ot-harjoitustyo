import pygame
import os

class Download_pictures:
    def __init__(self):
        self.mehilainen = pygame.image.load("src/pictures/mehilainen.png")
        self.mehilainencopy = self.mehilainen.copy()
        self.mehilainencopy = pygame.transform.flip(self.mehilainen,True, False)
        self.kukka = pygame.image.load("src/pictures/kukka.png")
        self.pisara = pygame.image.load("src/pictures/pisara.png")
