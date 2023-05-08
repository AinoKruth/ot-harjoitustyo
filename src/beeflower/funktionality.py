import pygame
from random import randint
from creativity import Creativity

class BeeFlower:

    #initializing the game
    def __init__(self):

        pygame.init()
        self.Creativity = Creativity()

        self.highscore = 0
        self.height = 480
        self.width = 640

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.go = True
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("BeeFlower")

        self.go = True
        self.new_game()
        self.loop()

#starting the game
    def start(self):
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
            self.Creativity.starttext()
    #Defining the starting points:
    def new_game(self):
        self.Creativity.draw_screen()
        self.Creativity.points = 0
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
            self.Creativity.draw_screen()

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
            self.Creativity.x += 2
        if self.left:
            self.Creativity.x -= 2
        if self.up:
            self.Creativity.y -= 2
        if self.down:
            self.Creativity.y += 2

	#pidetään hahmo sisällä

        if self.Creativity.x <= 0:
            self.left = False
        if self.Creativity.x >= 570:
            self.right = False
        if self.Creativity.y <= 0:
            self.up = False
        if self.Creativity.y >= 405:
            self.down = False

        #If the game is not over or passed, defining the events
        if self.go == True:

            #Defining how fast the flowers drop, and making it quicker after every 5 flower that were catched:
            for i in range(self.Creativity.amounth):
                if self.Creativity.points >= 15:
                    self.Creativity.places[i][1] +=3
                if self.Creativity.points >= 10:
                    self.Creativity.places[i][1] +=2
                if self.Creativity.points >= 5:
                    self.Creativity.places[i][1] +=1.5
                else:
                    self.Creativity.places[i][1] += 1

                #Defining the starting point of the flower
                if self.Creativity.places[i][1]+self.Creativity.kukka.get_height() >= self.height:
                    self.Creativity.places[i][0] = randint(0,self.width-self.Creativity.kukka.get_width())
                    self.Creativity.places[i][1] = -randint(100,1000)

                #Defining what happens when the bee gets the flower:
                if self.Creativity.places[i][1]+self.Creativity.kukka.get_height()-25 >= self.Creativity.y:
                    if self.Creativity.y+self.Creativity.mehilainen.get_height()-25 >= self.Creativity.places[i][1]:
                        mehilainen_middle = self.Creativity.x+self.Creativity.mehilainen.get_width()/2
                        kukka_middle = self.Creativity.places[i][0]+self.Creativity.kukka.get_width()/2
                        if abs(mehilainen_middle-kukka_middle) <= (self.Creativity.mehilainen.get_width()+self.Creativity.kukka.get_width())/2-22:

                        #Defining a new starting point to the flower
                            self.Creativity.places[i][0] = randint(0,self.width-self.Creativity.kukka.get_width())
                            self.Creativity.places[i][1] = -randint(100,1000)
                            self.Creativity.points += 1

            #Defining how fast the waterdrops drop, and making it quicker after every 5 flower that were catched:
            for i in range(self.Creativity.amounth1):
                if self.Creativity.points >= 15:
                    self.Creativity.places1[i][1] +=3
                if self.Creativity.points >= 10:
                    self.Creativity.places1[i][1] +=2
                if self.Creativity.points >= 5:
                    self.Creativity.places1[i][1] +=1.5
                else:
                    self.Creativity.places1[i][1] += 1

                #Defining the starting point of the waterdrop:
                if self.Creativity.places1[i][1]+self.Creativity.pisara.get_height() >= self.height:
                    self.Creativity.places1[i][0] = randint(0,self.width-self.Creativity.pisara.get_width())
                    self.Creativity.places1[i][1] = -randint(100,1000)

                #Defining the game to end when the bee hits a waterdrop:
                if self.Creativity.places1[i][1]+self.Creativity.pisara.get_height()-25 >= self.Creativity.y:
                    if self.Creativity.y+self.Creativity.mehilainen.get_height()-25  >= self.Creativity.places1[i][1]:
                        mehilainen_middle = self.Creativity.x+self.Creativity.mehilainen.get_width()/2
                        pisara_keski = self.Creativity.places1[i][0]+self.Creativity.pisara.get_width()/2
                        if abs(mehilainen_middle-pisara_keski) <= (self.Creativity.mehilainen.get_width()+self.Creativity.pisara.get_width())/2-25:
                            self.go = False

    #Defining highscore and end of the game
    def end_game(self):
        if self.go == False:
            if self.Creativity.points > self.highscore:
                points = self.Creativity.points
                self.highscore = points
            return True
        else:
            return False
        self.Creativity.lose()
    #Defining what happens when you win the game
    def game_passed(self):

        if self.Creativity.points == 20:
            self.go = False
            return True
        else:
            return False
        self.Creativity.passed()

if __name__ == "__main__":
    BeeFlower()
