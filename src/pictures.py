import pygame

class DownloadPictures:
    #Downloading the pictures of the game
    def __init__(self):
        self.mehilainen = pygame.image.load("src/pictures/mehilainen.png")
        self.mehilainencopy = self.mehilainen.copy()
        self.mehilainencopy = pygame.transform.flip(self.mehilainen,True, False)
        self.kukka = pygame.image.load("src/pictures/kukka.png")
        self.pisara = pygame.image.load("src/pictures/pisara.png")
