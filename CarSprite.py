from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from Line import *
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
    def draw(self):
        self.carSprite.draw()
        thetaRadian = -math.radians(self.getTheta())
        deltaX = math.cos(thetaRadian) * 50 
        deltaY = math.sin(thetaRadian) * 50




        deltaX3 = math.cos(thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY3 = math.sin(thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)
        X3=self.getX()-deltaX3
        Y3=self.getY()-deltaY3
        print(str(X3)+ " "+ str(X3)+ " "+ str(thetaRadian/math.pi)+" "+str((thetaRadian+math.pi)/math.pi) + " " + str(math.sqrt(deltaX3*deltaX3+deltaY3*deltaY3)))
        
        #bottom horizontal line at point(X3,Y3)
        Line(X3,Y3,X3+deltaX, Y3 +deltaY,[0,0,0],1).draw()


        deltaX4 = math.cos(thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY4 = math.sin(thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        X4=self.getX()-deltaX4
        Y4=self.getY()-deltaY4

        #top horizontal line at point(X4,Y4)
        Line(X4,Y4,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()

        #left vertical line
        Line(X3,Y3,X4,Y4,[0,0,0],1).draw()
        
        #right vertical line
        Line(X3+deltaX, Y3 +deltaY ,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()

        deltaXVision = math.cos(thetaRadian) * 100 
        deltaYVision = math.sin(thetaRadian) * 100
        
        
        #middle vision line
        deltaX2 = math.cos(thetaRadian) * 50/2
        deltaY2 = math.sin(thetaRadian) * 50/2
        X2=self.getX()-deltaXVision
        Y2=self.getY()-deltaYVision
        Line(X2,Y2,self.getX()+deltaXVision,self.getY()+deltaYVision,[0,0,0],1).draw()



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