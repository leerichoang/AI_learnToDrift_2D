from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from Line import *

class CarVision:
    def __init__(self):
        self.boundX1=[0,0]
        self.boundY1=[0,0]
        self.boundX2=[0,0]
        self.boundY2=[0,0]

    def draw(self, x, y, thetaR):
        self.thetaRadian=thetaR
        self.X=x
        self.Y=y
        deltaX = math.cos(self.thetaRadian) * 50 
        deltaY = math.sin(self.thetaRadian) * 50

        deltaX3 = math.cos(self.thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY3 = math.sin(self.thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)

        X3=self.X-deltaX3
        Y3=self.Y-deltaY3

        #top horizontal line at point(X3,Y3)
        Line(X3,Y3,X3+deltaX, Y3 +deltaY,[0,0,0],1).draw()

        deltaX4 = math.cos(self.thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY4 = math.sin(self.thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        X4=self.X-deltaX4
        Y4=self.Y-deltaY4

        #top horizontal line at point(X4,Y4)
        Line(X4,Y4,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()

        #left vertical line
        Line(X3,Y3,X4,Y4,[0,0,0],1).draw()

        #right vertical line
        Line(X3+deltaX, Y3 +deltaY ,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()

        
        #y=mx+b
        #b=y - mx
        #x = (b-y)/m
        slope=math.tan(self.thetaRadian)
        b = self.Y - slope*self.X
        #2
        if (slope>=0) and  (math.cos(self.thetaRadian) >= 0) and (math.sin(self.thetaRadian) >= 0):
            manitude = (1240-self.X)/math.cos(self.thetaRadian)
        elif (slope<0) and  (math.cos(self.thetaRadian) >= 0) and (math.sin(self.thetaRadian) < 0):
            manitude = (1240-self.X)/math.cos(self.thetaRadian)
        #1
        elif (slope>=0) and  (math.cos(self.thetaRadian) < 0) and (math.sin(self.thetaRadian) < 0):
            manitude = (40-self.X)/math.cos(self.thetaRadian)
        elif (slope<0) and  (math.cos(self.thetaRadian) <0) and (math.sin(self.thetaRadian) >= 0):
            manitude = (40-self.X)/math.cos(self.thetaRadian)
            
        #8
        if slope!=0:
            testxbounce = (260-b)/slope
        else:
            testxbounce = (260-b)        
        if int(testxbounce) in range(240,1040):
            if not (slope<0) and  (math.cos(self.thetaRadian) > 0) and (math.sin(self.thetaRadian) > 0):
                print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian)) 
            if (slope<0) and  (math.cos(self.thetaRadian) < 0) and (math.sin(self.thetaRadian) >= 0):
                print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian)) 
            print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
        
        #4
        if slope!=0:
            testxbounce = (60-b)/slope
        else:
            testxbounce = (60-b)
        if int(testxbounce) in range(40,1240):
            if (slope<0) and  (math.cos(self.thetaRadian) >= 0) and (math.sin(self.thetaRadian) < 0):
                print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian))
            if (slope>=0) and  (math.cos(self.thetaRadian) < 0) and (math.sin(self.thetaRadian) < 0):
                print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian)) 

        
        
        deltaXVision = math.cos(self.thetaRadian) * manitude
        deltaYVision = math.sin(self.thetaRadian) * manitude
        
        
        #middle vision line
        # deltaX2 = math.cos(self.thetaRadian) * 50/2
        # deltaY2 = math.sin(self.thetaRadian) * 50/2
        # X2=self.X-deltaXVision
        # Y2=self.Y-deltaYVision
        # Line(X2,Y2,self.X+deltaXVision,self.Y+deltaYVision,[0,0,0],1).draw()

        deltaX2 = math.cos(self.thetaRadian) * 50/2
        deltaY2 = math.sin(self.thetaRadian) * 50/2
        X2=self.X
        Y2=self.Y
        Line(X2,Y2,self.X+deltaXVision,self.Y+deltaYVision,[0,0,0],1).draw()
        print(str(int(X2))+ " "+str(int(Y2))+ " "+ str(int(deltaXVision))+ " "+str(int(deltaYVision)) + " " + str(self.thetaRadian) + " "+ str(slope))
        self.boundX1=[X3,Y3]
        self.boundY1=[X3+deltaX,Y3 +deltaY]
        self.boundX2=[X4,Y4]
        self.boundY2=[X4+deltaX, Y4 +deltaY]



