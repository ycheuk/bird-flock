from Bird import Bird
from Body import Body
from geometry import *
from Flock import Flock

EPSILON = 0.000001

class Obstacle(Body):
    def __init__(self,flock,world):
        Body.__init__(self,p0,v0,world)
        self.flock = flock
        self.world = world
        
    def shape(self):
        position1 = self.position + Vector2D(0.0,0.5)
        position2 = self.position + Vector2D(-3.0,5)
        position3 = self.position + Vector2D(0.0,-0.5)
        position4 = self.position + Vector2D(5.0,-0.5)
        return [position1,position2,position3,position4]

    def avoid(self,):
        for bird in self.flock:
            

class obstacleOne(Obstacle):
    def __init__(self,flock,world):
        Body.__init__(self,Point2D(-10.0,10.0),Vector2D(0.0,0.0),world)
        self.flock = flock
        self.world = world
        self.position = Point2D(0.0,0.0)

    def color(self):
        return "#0491AB"

class obstacleTwo(Obstacle):
    def __init__(self,flock,world):
        Body.__init__(self,Point2D(10.0,-10.0),Vector2D(0.0,0.0),world)
        self.flock = flock
        self.world = world
        self.position = Point2D(15.0,-15.0)

    def color(self):
        return "#0491AB"
