class gameloop:
    
    def __init__(self):
      
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

        #If the game is not over or passed, defining the events
        if self.go == True:

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

        if self.points == 50:
            self.go = False
            return True
        else:
            return False
    
    pygame.display.flip()
    self.clock.tick(60)
