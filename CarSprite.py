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
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, 100, 100)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
        self.speed = 100.0
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
        # if not self.carVision.isBothTrackCollision():
        #     self.updateTheta(-self.rotation_speed*dt)
        # else:
        #     self.updateTheta(self.rotation_speed *dt)
        self.updateTheta(-self.rotation_speed*dt)
        if self.carVision.isBothTrackCollision():
            self.updateTheta(self.rotation_speed* dt)


    def turnRight(self,dt):
        # if not self.carVision.isBothTrackCollision():
        #     self.updateTheta(self.rotation_speed* dt)
        # else:
        #     self.updateTheta(-self.rotation_speed * dt)
        self.updateTheta(self.rotation_speed* dt)
        if self.carVision.isBothTrackCollision():
            self.updateTheta(-self.rotation_speed*dt)

    def goStraight(self,dt):
        #if not (self.carVision.isBothTrackCollision()) and self.carVision.getDistanceFromColorLine("TEAL")>=0:
    
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        print("yelp")
        self.updateX(deltaX)
        self.updateY(deltaY)
        self.updateDeltaX(deltaX)
        self.updateDeltaY(deltaY)
        if self.carVision.isBothTrackCollision():
            thetaRadian = -math.radians(self.getTheta())
            deltaX = math.cos(thetaRadian) * self.speed * dt
            deltaY = math.sin(thetaRadian) * self.speed * dt
            self.updateX(-deltaX)
            self.updateY(-deltaY)
            self.updateDeltaX(-deltaX)
            self.updateDeltaY(-deltaY)




        # else:
        #     if self.carVision.getDistanceFromColorLine("RED")>=0:
        #         # thetaRadian = -math.radians(self.getTheta())
        #         # deltaX = math.cos(thetaRadian) * 20
        #         # deltaY = math.sin(thetaRadian) * 20
        #         # self.updateX(-deltaX)
        #         # self.updateY(-deltaY)
        #         # self.updateDeltaX(-deltaX)
        #         # self.updateDeltaY(-deltaY)
        #         self.goReverse(dt)
    
    def goReverse(self,dt):
        # if not self.carVision.isBothTrackCollision():
        #     thetaRadian = -math.radians(self.getTheta())
        #     deltaX = math.cos(thetaRadian) * self.speed * dt
        #     deltaY = math.sin(thetaRadian) * self.speed * dt
        #     self.updateX(-deltaX)
        #     self.updateY(-deltaY)
        #     self.updateDeltaX(-deltaX)
        #     self.updateDeltaY(-deltaY)
        # else:
        #     thetaRadian = -math.radians(self.getTheta())
        #     deltaX = math.cos(thetaRadian) * self.speed * dt
        #     deltaY = math.sin(thetaRadian) * self.speed * dt
        #     print("yelp")
        #     self.updateX(deltaX)
        #     self.updateY(deltaY)
        #     self.updateDeltaX(deltaX)
        #     self.updateDeltaY(deltaY)
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * self.speed * dt
        deltaY = math.sin(thetaRadian) * self.speed * dt
        self.updateX(-deltaX)
        self.updateY(-deltaY)
        self.updateDeltaX(-deltaX)
        self.updateDeltaY(-deltaY)
        if self.carVision.isBothTrackCollision() and self.carVision.getDistanceFromColorLine("TEAL")>=0:
            thetaRadian = -math.radians(self.getTheta())
            deltaX = math.cos(thetaRadian) * self.speed * dt
            deltaY = math.sin(thetaRadian) * self.speed * dt
            print("yelp")
            self.updateX(deltaX)
            self.updateY(deltaY)
            self.updateDeltaX(deltaX)
            self.updateDeltaY(deltaY)

    def runningCar(self,dt):
        self.updateX(self.getDeltaX())
        self.updateY(self.getDeltaY())
        self.updateDeltaX(self.getDeltaX() * 0.10)
        self.updateDeltaY(self.getDeltaY() * 0.10)