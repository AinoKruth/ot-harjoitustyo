import pygame
from random import randint


class beeflower:

    # initializing the game
    def __init__(self):

        pygame.init()
        self.download_pictures()

        self.highscore = 0
        self.hight = 480
        self.width = 640
        self.x = 0
        self.y = self.hight-self.mehilainen.get_height()

        self.screen = pygame.display.set_mode((self.width, self.hight))
        self.font = pygame.font.SysFont("Arial", 26)
        self.font2 = pygame.font.SysFont("Arial", 30)
        self.font3 = pygame.font.SysFont("Arial", 28)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("BeeFlower")

        self.go = True
        self.starttext()
        self.new_game()
        self.loop()
        
        
    #Downloading the pictures to the game
    
    def download_pictures(self):
        self.mehilainen = pygame.image.load("mehilainen.png")
        self.kukka = pygame.image.load("kukka.png")
        self.pisara = pygame.image.load("pisara.png")

        # Building the text:
    def starttext(self):
        start = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start = True
            if start == True:
                break
            self.screen.fill((222, 33, 153))
            pygame.draw.rect(self.screen, (80, 12, 55), (10, 10, 620, 460))
            pygame.draw.rect(self.screen, (188, 25, 128), (15, 15, 610, 450))
            text = self.font2.render(
                "Betty bees honey has ended,", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 100))
            text = self.font2.render(
                "and she needs more flowers!", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 150))
            text = self.font2.render(
                " Collect betty 20 flowers,", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 200))
            text = self.font2.render(
                "so she can make a carton of honey again.", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 250))
            text = self.font2.render(
                "But beware of the waterdrops!", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 300))
            text = self.font2.render(
                "You can start the game by pressing enter.", True, (80, 12, 55))
            self.screen.blit(
                text, (self.width / 2 - text.get_width() / 2, 350))
            pygame.display.flip()

    # Drawing the screen
    def draw_screen(self):

        self.screen.fill((222, 33, 153))
        self.screen.blit(self.mehilainen, (self.x, self.y))
        for i in range(self.amounth):
            self.screen.blit(
                self.kukka, (self.places[i][0], self.places[i][1]))
        for i in range(self.amounth):
            self.screen.blit(
                self.pisara, (self.places1[i][0], self.places1[i][1]))


if __name__ == "__main__":
    beeflower()
