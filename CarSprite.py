from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
WINDOWWIDTH=1280
WINDOWHEIGHT=720 
class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite_resized10percent.png')
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 0, self.carSprite_image.height)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
        self.speed = 200.0
        self.rotation_speed = 200.0
        self.deltaX = 0.0
        self.deltaY = 0.0
        print(self.carSprite.width)
        print(self.carSprite.height)
        self.width = self.carSprite.width
        self.height = self.carSprite.height
    def draw(self):
        self.carSprite.draw()
    
    def getX(self):
        self.x = self.carSprite.x
        return self.x
    def getY(self):
        self.y = self.carSprite.y
        return self.y
    def getTheta(self):
        self.theta = self.carSprite.rotation
        return self.theta

    def getDeltaX(self):
        return self.deltaX
    def getDeltaY(self):
        return self.deltaY


    def updateX(self,value):
        value += self.getX()
        if value + self.carSprite_image.width >WINDOWWIDTH:
            print("out of bounce " + " "+ str(self.getTheta()))
        self.carSprite.update(x=value)
    def updateY(self,value):
        value += self.getY()
        self.carSprite.update(y=value)
    def updateTheta(self,degree):  
        degree += self.getTheta()
        self.carSprite.update(rotation=degree)
    def updateDeltaX(self, value):
        self.deltaX = value
    def updateDeltaY(self, value):
        self.deltaY = value

    def turnLeft(self,dt):
        self.updateTheta(-self.rotation_speed* dt)

    def turnRight(self,dt):
        self.updateTheta(self.rotation_speed* dt)
    
    def goStraight(self,dt):
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        self.updateX(deltaX)
        self.updateY(deltaY)
        self.updateDeltaX(deltaX)
        self.updateDeltaY(deltaY)
    
    def goReverse(self,dt):
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        self.updateX(-deltaX)
        self.updateY(-deltaY)
        self.updateDeltaX(-deltaX)
        self.updateDeltaY(-deltaY)  

    def runningCar(self,dt):
        self.updateX(self.getDeltaX())
        self.updateY(self.getDeltaY())
        self.updateDeltaX(self.getDeltaX() * 0.95)
        self.updateDeltaY(self.getDeltaY() * 0.95)