from random import randint
import pygame

from pictures import DownloadPictures

class Events:

    def __init__(self,Bee,Keys):
        self.bee = Bee
        self.dp = DownloadPictures()
        self.keys = Keys
        self.points = 0
        self.go = True
        self.highscore = 0
        self.height = 480
        self.width = 649
        self.amounth = 5
        self.amounth1 = 5
        self.places = []
        self.places1 = []
        self.clock = pygame.time.Clock()

    #Defining the starting points on a new game
    def new_game(self):
        self.bee.x = 0
        self.bee.y = 405
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


    #defining the pausing of the game
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


    #Defining the end of the game
    def end_game(self):
        if not self.go:
            if self.points > self.highscore:
                points = self.points
                self.highscore = points
            return True

        return False

    #Defining the winning of the game
    def game_passed(self):

        if self.points == 20:
            self.go = False
            return True

        return False

    #Defining the events
    def see_event(self):

        if self.game_passed():
            self.go = False

        self.keys.keys(self)
        self.bee.liiku()

        #If the game is not over or passed, defining the events
        if self.go:
            self.flower_waterdrop()


    def flower_waterdrop(self):

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
            if self.places[i][1]+self.dp.kukka.get_height() >= self.height:
                self.places[i][0] = randint(0,self.width-self.dp.kukka.get_width())
                self.places[i][1] = -randint(100,1000)

            #Defining what happens when the bee gets the flower:
            if self.places[i][1]+self.dp.kukka.get_height()-25 >= self.bee.y:
                if self.bee.y+self.dp.mehilainen.get_height()-25 >= self.places[i][1]:
                    mehilainen_middle = self.bee.x+self.dp.mehilainen.get_width()/2
                    kukka_middle = self.places[i][0]+self.dp.kukka.get_width()/2
                    if abs(mehilainen_middle-kukka_middle) <= (self.dp.mehilainen.get_width()+self.dp.kukka.get_width())/2-22:
                         #Defining a new starting point to the flower
                        self.places[i][0] = randint(0,self.width-self.dp.kukka.get_width())
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
            if self.places1[i][1]+self.dp.pisara.get_height() >= self.height:
                self.places1[i][0] = randint(0,self.width-self.dp.pisara.get_width())
                self.places1[i][1] = -randint(100,1000)

            #Defining the game to end when the bee hits a waterdrop:
            if self.places1[i][1]+self.dp.pisara.get_height()-25 >= self.bee.y:
                if self.bee.y+self.dp.mehilainen.get_height()-25  >= self.places1[i][1]:
                    mehilainen_middle = self.bee.x+self.dp.mehilainen.get_width()/2
                    pisara_keski = self.places1[i][0]+self.dp.pisara.get_width()/2
                    if abs(mehilainen_middle-pisara_keski) <= (self.dp.mehilainen.get_width()+self.dp.pisara.get_width())/2-25:
                        self.go = False
