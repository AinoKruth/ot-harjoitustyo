import pygame

class Download_pictures:
    def __init__(self):
        self.mehilainen = pygame.image.load("pictures/mehilainen.png")
        self.mehilainencopy = self.mehilainen.copy()
        self.mehilainencopy = pygame.transform.flip(self.mehilainen,True, False)
        self.kukka = pygame.image.load("pictures/kukka.png")
        self.pisara = pygame.image.load("pictures/pisara.png")
