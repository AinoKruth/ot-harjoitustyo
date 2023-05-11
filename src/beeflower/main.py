import pygame
from random import randint

from bee import Bee
from pictures import Download_pictures
from events import Events
from draw import Draw
from keys import Keys

class BeeFlower:

    #initializing the game
    def __init__(self):

        pygame.init()
        self.dp = Download_pictures()
        self.bee = Bee()
        self.events = Events(self.bee, Keys)
        self.draw = Draw(self.events, self.dp, self.bee)
        self.keys = Keys(self.events, self.bee)
        pygame.display.set_caption("BeeFlower")

        self.draw.starttext()
        self.events.new_game()
        self.loop()

    #Defining the loop of the game:
    def loop(self):
        while True:
            self.events.see_event()
            self.draw.draw_screen()



if __name__ == "__main__":
    BeeFlower()