import pygame

class Draw:

    def __init__(self, Events, Download_pictures, Bee):

        self.height = 480
        self.width = 640

        self.events = Events
        self.dp = Download_pictures
        self.bee = Bee
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("Arial", 26)
        self.font2 = pygame.font.SysFont("Arial", 30)
        self.font3 = pygame.font.SysFont("Arial", 28)


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
            if start:
                break
            self.screen.fill((222, 33, 153))
            pygame.draw.rect(self.screen, (80, 12, 55), (10,10,620,460))
            pygame.draw.rect(self.screen, (188, 25, 128), (15,15,610,450))
            text = self.font2.render("Betty Bees honey is all gone,", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,100))
            text = self.font2.render("and she needs more flowers!", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,150))
            text = self.font2.render("Collect Betty 20 flowers,", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,200))
            text = self.font2.render("so she can make a carton of honey again.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,250))
            text = self.font2.render("Beware of the waterdrops!", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,300))
            text = self.font2.render("You can start the game by pressing enter.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2, 350))
            pygame.display.flip()
            self.events.inpt()

    #Drawing the screen
    def draw_screen(self):

        self.screen.fill((222, 33, 153))
        if self.bee.left:
            self.screen.blit(self.dp.mehilainencopy, (self.bee.x, self.bee.y))
        else:
            self.screen.blit(self.dp.mehilainen, (self.bee.x, self.bee.y))
        for i in range(self.events.amounth):
            self.screen.blit(self.dp.kukka, (self.events.places[i][0], self.events.places[i][1]))
        for i in range(self.events.amounth):
            self.screen.blit(self.dp.pisara, (self.events.places1[i][0], self.events.places1[i][1]))

        #Defining the lower text:
        text = self.font.render("Points: " + str(self.events.points), True, (80, 12, 55))
        self.screen.blit(text, (10, self.height-30))

        text = self.font.render("P = Pause" , True, (80, 12, 55))
        self.screen.blit(text, (140, self.height-30))

        text = self.font.render("C = Continue", True, (80, 12, 55))
        self.screen.blit(text, (290, self.height-30))

        text = self.font.render("Esc = End Game ", True, (80, 12, 55))
        self.screen.blit(text, (460, self.height-30))

        #Defining the screen and the text when the game ends.

        if self.events.end_game():
            #If you win the game:
            if self.events.game_passed():
                pygame.draw.rect(self.screen, (80, 12, 55), (60,155,532,180))
                pygame.draw.rect(self.screen, (188, 25, 128), (65,160,522,170))
                text = self.font2.render("Betty is a happy bee with all of her honey!", True, ((80, 12, 55)))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2 ,223))
            #And if you lose the game
            else:
                pygame.draw.rect(self.screen, (80, 12, 55), (60,145,532,180))
                pygame.draw.rect(self.screen, (188, 25, 128), (65,150,522,170))
                text = self.font2.render("Oh no! Betty got wet!!", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,175))
                text = self.font3.render(f"High Score: {self.events.highscore}", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,220))
                text = self.font3.render("New Game? Press n.", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,260))

        pygame.display.flip()
        self.events.clock.tick(60)
