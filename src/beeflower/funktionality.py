import pygame
from random import randint


class BeeFlower:

    #initializing the game
    def __init__(self):

        pygame.init()
        self.download_pictures()

        self.highscore = 0
        self.height = 480
        self.width = 640
        self.x = 0
        self.y = self.height-self.mehilainen.get_height()

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.points = 0
        self.go = True

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("Arial", 26)
        self.font2 = pygame.font.SysFont("Arial", 30)
        self.font3 = pygame.font.SysFont("Arial", 28)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("BeeFlower")

        self.go = True
        self.starttext()
        self.new_game()
        self.loop()

    #Defining the starting points:
    def new_game(self):
        self.x = 0
        self.y = 480-self.mehilainen.get_height()
        self.amounth = 5
        self.amounth1 = 5

        self.places = []
        self.places1 = []

        for i in range(self.amounth):
            self.places.append([randint(0,590),-randint(100,1000)])

        for i in range(self.amounth1):
            self.places1.append([randint(100,400),-randint(100,1000)])
        self.points = 0
        self.go = True
    #defining how to pause game
    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
            pygame.display.update()
            self.clock.tick(5)


    #Defining the loop of the game:
    def loop(self):
        while True:
            self.see_event()
            self.draw_screen()

    #Defining the events and keys of the game:
    def see_event(self):
        #Looking if the game is over or passed
        if self.game_passed():
            self.go = False

        #Keys of the game
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if self.go == True:
                    if event.key == pygame.K_LEFT:
                        self.left = True
                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    if event.key == pygame.K_UP:
                        self.up = True
                    if event.key == pygame.K_DOWN:
                        self.down = True
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_n:
                    self.new_game()
                if event.key == pygame.K_p:
                    self.pause()
                if event.key == pygame.K_c:
                    self.pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False

            if event.type == pygame.QUIT:
                exit()

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

        #If the game is not over or passed, defining the events
        if self.go == True:

            #Defining how fast the flowers drop, and making it quicker after every 5 flower that were catched:
            for i in range(self.amounth):
                if self.points >= 15:
                    self.places[i][1] +=3
                if self.points >= 10:
                    self.places[i][1] +=2
                if self.points >= 5:
                    self.places[i][1] +=1.5
                else:
                    self.places[i][1] += 1

                #Defining the starting point of the flower
                if self.places[i][1]+self.kukka.get_height() >= self.height:
                    self.places[i][0] = randint(0,self.width-self.kukka.get_width())
                    self.places[i][1] = -randint(100,1000)

                #Defining what happens when the bee gets the flower:
                if self.places[i][1]+self.kukka.get_height()-25 >= self.y:
                    if self.y+self.mehilainen.get_height()-25 >= self.places[i][1]:
                        mehilainen_middle = self.x+self.mehilainen.get_width()/2
                        kukka_middle = self.places[i][0]+self.kukka.get_width()/2
                        if abs(mehilainen_middle-kukka_middle) <= (self.mehilainen.get_width()+self.kukka.get_width())/2-22:

                        #Defining a new starting point to the flower
                            self.places[i][0] = randint(0,self.width-self.kukka.get_width())
                            self.places[i][1] = -randint(100,1000)
                            self.points += 1

            #Defining how fast the waterdrops drop, and making it quicker after every 5 flower that were catched:
            for i in range(self.amounth1):
                if self.points >= 15:
                    self.places1[i][1] +=3
                if self.points >= 10:
                    self.places1[i][1] +=2
                if self.points >= 5:
                    self.places1[i][1] +=1.5
                else:
                    self.places1[i][1] += 1

                #Defining the starting point of the waterdrop:
                if self.places1[i][1]+self.pisara.get_height() >= self.height:
                    self.places1[i][0] = randint(0,self.width-self.pisara.get_width())
                    self.places1[i][1] = -randint(100,1000)

                #Defining the game to end when the bee hits a waterdrop:
                if self.places1[i][1]+self.pisara.get_height()-25 >= self.y:
                    if self.y+self.mehilainen.get_height()-25  >= self.places1[i][1]:
                        mehilainen_middle = self.x+self.mehilainen.get_width()/2
                        pisara_keski = self.places1[i][0]+self.pisara.get_width()/2
                        if abs(mehilainen_middle-pisara_keski) <= (self.mehilainen.get_width()+self.pisara.get_width())/2-25:
                            self.go = False

    #Defining highscore and end of the game
    def end_game(self):
        if self.go == False:
            if self.points > self.highscore:
                points = self.points
                self.highscore = points
            return True
        else:
            return False
    #Defining what happens when you win the game
    def game_passed(self):

        if self.points == 20:
            self.go = False
            return True
        else:
            return False

if __name__ == "__main__":
    BeeFlower()
