import pygame
from index import index 

class creativity:
    def __init__(self):

#Downloading the pictures to the game
    def download_pictures(self):
        self.mehilainen = pygame.image.load("mehilainen.png")
        self.kukka = pygame.image.load("kukka.png")
        self.pisara = pygame.image.load("pisara.png")

#Drawing the screen
    def draw_screen(self):

        self.screen.fill((222, 33, 153))
        self.screen.blit(self.mehilainen, (self.x, self.y))
        for i in range(self.amounth):
            self.screen.blit(self.kukka, (self.places[i][0], self.places[i][1]))
        for i in range(self.amounth):
            self.screen.blit(self.pisara, (self.places1[i][0], self.places1[i][1]))

        #Defining the lower text:
        text = self.font.render("points: " + str(self.points), True, (80, 12, 55))
        self.screen.blit(text, (35, self.hight-30))

        text = self.font.render("N = New Game", True, (80, 12, 55))
        self.screen.blit(text, (240, self.hight-30))

        text = self.font.render("Esc = Leave Game", True, (80, 12, 55))
        self.screen.blit(text, (450, self.hight-30))

#Building the start text:
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
            pygame.draw.rect(self.screen, (80, 12, 55), (10,10,620,460))
            pygame.draw.rect(self.screen, (188, 25, 128), (15,15,610,450))
            text = self.font2.render("Betty Bees honey is all gone,", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,100))
            text = self.font2.render("and she needs more flowers!", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,150))
            text = self.font2.render("Collect Bettu 20 flowers,", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,200))
            text = self.font2.render("so she can make a carton of honey again.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,250))
            text = self.font2.render("Beware of the waterdrops!", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,300))
            text = self.font2.render("You can start the game by pressing enter.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2, 350))
            pygame.display.flip()

#Defining the screen and the text when the game ends.
        if self.end_game():
            #If you win the game:
            if self.game_passed():
                pygame.draw.rect(self.screen, (80, 12, 55), (60,155,532,180))
                pygame.draw.rect(self.screen, (188, 25, 128), (65,160,522,170))
                text = self.font2.render("Congratulations! Betty is a happy bee with all her honey!", True, ((80, 12, 55)))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2 ,223))
#And if you lose the game
            else:
                pygame.draw.rect(self.screen, (80, 12, 55), (60,145,532,180))
                pygame.draw.rect(self.screen, (188, 25, 128), (65,150,522,170))
                text = self.font2.render("Oh no! Betty got wet!!", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,175))
                text = self.font3.render(f"High Score: {self.highscore}", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,220))
                text = self.font3.render("New Game?", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,260))
