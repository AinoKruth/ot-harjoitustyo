    #Downloading the pictures to the game
    def download_pictures(self):
        self.mehilainen = pygame.image.load("mehilainen.png")
        self.mehilainencopy = self.mehilainen.copy()
        self.mehilainencopy = pygame.transform.flip(self.mehilainen,True, False)
        self.kukka = pygame.image.load("kukka.png")
        self.pisara = pygame.image.load("pisara.png")

    #Building the text:
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
            text = self.font2.render("Collect Betty 20 flowers,", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,200))
            text = self.font2.render("so she can make a carton of honey again.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,250))
            text = self.font2.render("Beware of the waterdrops!", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2,300))
            text = self.font2.render("You can start the game by pressing enter.", True, (80, 12, 55))
            self.screen.blit(text,(self.width / 2 - text.get_width() / 2, 350))
            pygame.display.flip()

    #Drawing the screen
    def draw_screen(self):

        self.screen.fill((222, 33, 153))
        if self.left == True:
            self.screen.blit(self.mehilainencopy, (self.x, self.y))
        else:
            self.screen.blit(self.mehilainen, (self.x, self.y))
        for i in range(self.amounth):
            self.screen.blit(self.kukka, (self.places[i][0], self.places[i][1]))
        for i in range(self.amounth):
            self.screen.blit(self.pisara, (self.places1[i][0], self.places1[i][1]))

        #Defining the lower text:
        text = self.font.render("Points: " + str(self.points), True, (80, 12, 55))
        self.screen.blit(text, (10, self.height-30))

        text = self.font.render("P = Pause" , True, (80, 12, 55))
        self.screen.blit(text, (140, self.height-30))

        text = self.font.render("C = Continue", True, (80, 12, 55))
        self.screen.blit(text, (290, self.height-30))

        text = self.font.render("Esc = End Game ", True, (80, 12, 55))
        self.screen.blit(text, (460, self.height-30))

        #Defining the screen and the text when the game ends.
        if self.end_game():
            #If you win the game:
            if self.game_passed():
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
                text = self.font3.render(f"High Score: {self.highscore}", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,220))
                text = self.font3.render("New Game? Press n.", True, (80, 12, 55))
                self.screen.blit(text,(self.width / 2 - text.get_width()/2,260))
        pygame.display.flip()
        self.clock.tick(60)
