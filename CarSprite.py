from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from Line import *
from CarVision import *
WINDOWWIDTH=1280
WINDOWHEIGHT=720 
class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite5050.png')
        self.carSprite_image.anchor_x=25
        self.carSprite_image.anchor_y=25
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 40+25, 60+25)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
        self.speed = 200.0
        self.rotation_speed = 220.0
        self.deltaX = 0.0
        self.deltaY = 0.0
        print(self.carSprite.width)
        print(self.carSprite.height)
        self.width = self.carSprite.width
        self.height = self.carSprite.height
        self.carVision=CarVision()
    def draw(self):
        self.carSprite.draw()
        thetaRadian = -math.radians(self.getTheta())
        self.carVision.draw(self.getX(),self.getY(),thetaRadian)


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
        #print(str(self.getX())+ " "+ str(self.getY()))

    def turnRight(self,dt):
        self.updateTheta(self.rotation_speed* dt)
        #print(str(self.getX())+ " "+ str(self.getY()))
    
    def goStraight(self,dt):
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        self.updateX(deltaX)
        self.updateY(deltaY)
        self.updateDeltaX(deltaX)
        self.updateDeltaY(deltaY)
        #print(str(self.getX())+ " "+ str(self.getY()))
    
    def goReverse(self,dt):
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        self.updateX(-deltaX)
        self.updateY(-deltaY)
        self.updateDeltaX(-deltaX)
        self.updateDeltaY(-deltaY)  
        #print(str(self.getX())+ " "+ str(self.getY()))

    def runningCar(self,dt):
        self.updateX(self.getDeltaX())
        self.updateY(self.getDeltaY())
        self.updateDeltaX(self.getDeltaX() * 0.95)
        self.updateDeltaY(self.getDeltaY() * 0.95)