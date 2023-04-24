class index:
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


        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.points = 0
        self.go = True
