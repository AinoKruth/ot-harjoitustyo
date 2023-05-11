import pygame

class Keys:

    def __init__(self,Bee,Events):
        self.bee = Bee
        self.event = Events

    #Defining the keys of the game
    def keys(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if self.event.go:
                    if event.key == pygame.K_LEFT:
                        self.bee.left = True
                    if event.key == pygame.K_RIGHT:
                        self.bee.right = True
                    if event.key == pygame.K_UP:
                        self.bee.up = True
                    if event.key == pygame.K_DOWN:
                        self.bee.down = True

                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_n:
                    self.event.new_game()
                if event.key == pygame.K_p:
                    self.event.pause()
                if event.key == pygame.K_c:
                    self.event.pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.bee.left = False
                if event.key == pygame.K_RIGHT:
                    self.bee.right = False
                if event.key == pygame.K_UP:
                    self.bee.up = False
                if event.key == pygame.K_DOWN:
                    self.bee.down = False

            if event.type == pygame.QUIT:
                exit()