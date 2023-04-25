import pygame


class movement:

    def __init__(self):
          None  
#Defining the movement of the bee
    def moveright(self):
        x += 2
        return x
    def moveleft(self):
        x -= 2
        return x
    def moveup(self):
        y -= 2
        return y
    def movedown(self):
        y += 2
        return y


#Defining the bee to stay inside the walls
    def keep_inside(self):
        if x <= 0:
            self.left = False
        if self.x >= 570:
            self.right = False
        if self.y <= 0:
            self.up = False
        if self.y >= 405:
            self.down = False


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
        if self.places[i][1]+self.kukka.get_height() >= self.hight:
            self.places[i][0] = randint(0,self.width-self.kukka.get_width())
            self.places[i][1] = -randint(100,1000)

#Defining what happens when the bee gets the flower:
        if self.places[i][1]+self.kukka.get_height() >= self.y and self.y+self.mehilainen.get_height() >= self.places[i][1]:
            mehilainen_middle = self.x+self.mehilainen.get_width()/2
            kukka_middle = self.places[i][0]+self.kukka.get_width()/2
            if abs(mehilainen_middle-kukka_middle) <= (self.mehilainen.get_width()+self.kukka.get_width())/2:

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
        if self.places1[i][1]+self.pisara.get_height() >= self.hight:
            self.places1[i][0] = randint(0,self.width-self.pisara.get_width())
            self.places1[i][1] = -randint(100,1000)
