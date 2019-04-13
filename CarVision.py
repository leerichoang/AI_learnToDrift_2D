from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from Line import *

class CarVision:
    def __init__(self):
        self.carBoxX1=[0,0]
        self.carBoxY1=[0,0]
        self.carBoxX2=[0,0]
        self.carBoxY2=[0,0]
    
    def drawCarBox(self):
        # Y1 - - Y2
        # |      |
        # |      |
        # X1 - - X2

        deltaX = math.cos(self.thetaRadian) * 50 
        deltaY = math.sin(self.thetaRadian) * 50

        deltaX3 = math.cos(self.thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY3 = math.sin(self.thetaRadian+math.pi/4) * math.sqrt((50/2*50/2)*2)

        X3=self.X-deltaX3
        Y3=self.Y-deltaY3

        #top horizontal line from X1 to X2 
        Line(X3,Y3,X3+deltaX, Y3 +deltaY,[0,0,0],1).draw()

        deltaX4 = math.cos(self.thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        deltaY4 = math.sin(self.thetaRadian-math.pi/4) * math.sqrt((50/2*50/2)*2)
        X4=self.X-deltaX4
        Y4=self.Y-deltaY4

        #top horizontal line at Y1 to Y2 
        Line(X4,Y4,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()

        #left vertical line at X1 to Y1 
        Line(X3,Y3,X4,Y4,[0,0,0],1).draw()

        #right vertical line X2 to Y2 
        Line(X3+deltaX, Y3 +deltaY ,X4+deltaX, Y4 +deltaY,[0,0,0],1).draw()
        
        #update carBox Coordinates
        self.carBoxX1=[X3,Y3]
        self.carBoxY1=[X4,Y4]
        self.carBoxX2=[X3+deltaX,Y3 +deltaY]
        self.carBoxY2=[X4+deltaX,Y4 +deltaY]

    def drawVisionLine(self):
        for i in range(-4,4,1):
            rToAdd = i * math.pi/4 
            #rToAdd = 0 * math.pi/4 
            
            #y=mx+b
            #b=y - mx
            #x = (b-y)/m
            
            #find slope
            slope=math.tan(self.thetaRadian + rToAdd)

            #find y intercept b=y - mx
            b = self.Y - slope*self.X

            #2 check for vertical line at 1240
            if (slope>=0) and  (math.cos(self.thetaRadian+ rToAdd) >= 0) and (math.sin(self.thetaRadian+ rToAdd) >= 0):
                manitude = (1240-self.X)/math.cos(self.thetaRadian+ rToAdd)
            elif (slope<0) and  (math.cos(self.thetaRadian+ rToAdd) >= 0) and (math.sin(self.thetaRadian+ rToAdd) < 0):
                manitude = (1240-self.X)/math.cos(self.thetaRadian+ rToAdd)
            
            #1 check for vertical line at 40
            elif (slope>=0) and  (math.cos(self.thetaRadian+ rToAdd) < 0) and (math.sin(self.thetaRadian+ rToAdd) < 0):
                manitude = (40-self.X)/math.cos(self.thetaRadian+ rToAdd)
            elif (slope<0) and  (math.cos(self.thetaRadian+ rToAdd) <0) and (math.sin(self.thetaRadian+ rToAdd) >= 0):
                manitude = (40-self.X)/math.cos(self.thetaRadian+ rToAdd)
                
            #8 check for horizontal line at 240,260 to 1040 to 260
            if slope!=0:
                testxbounce = (260-b)/slope
            else:
                testxbounce = (260-b)        
            if int(testxbounce) in range(240,1040):
                if not (slope<0) and  (math.cos(self.thetaRadian+ rToAdd) > 0) and (math.sin(self.thetaRadian+ rToAdd) > 0):
                    #print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                    manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian+ rToAdd)) 
                if (slope<0) and  (math.cos(self.thetaRadian+ rToAdd) < 0) and (math.sin(self.thetaRadian+ rToAdd) >= 0):
                    #print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                    manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian+ rToAdd)) 
                #print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
            
            #4 check for horizontal line at 40,60 to 140 to 260 
            if slope!=0:
                testxbounce = (60-b)/slope
            else:
                testxbounce = (60-b)
            if int(testxbounce) in range(40,1240):
                if (slope<0) and  (math.cos(self.thetaRadian+ rToAdd) >= 0) and (math.sin(self.thetaRadian+ rToAdd) < 0):
                    #print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                    manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian+ rToAdd))
                if (slope>=0) and  (math.cos(self.thetaRadian+ rToAdd) < 0) and (math.sin(self.thetaRadian+ rToAdd) < 0):
                    #print(str(self.X) + " " + str(self.Y) + " " + str(slope) + " " +str(int(testxbounce)) + " hit " + str(math.sin(self.thetaRadian)) + " " + str(math.cos(self.thetaRadian)) )
                    manitude = ((testxbounce-self.X)/math.cos(self.thetaRadian+ rToAdd)) 

            
            #calculate the x and y 
            deltaXVision = math.cos(self.thetaRadian+ rToAdd) * manitude
            deltaYVision = math.sin(self.thetaRadian+ rToAdd) * manitude
                
            #draw the line
            Line(self.X,self.Y,self.X+deltaXVision,self.Y+deltaYVision,[0,0,0],1).draw()
            
            #calculate the distance = c
            # a^2 + b^2 = c^2
            # c = sqrt(a^2 + b^2)
            # - 25 for from the center
            distance = math.sqrt(deltaXVision*deltaXVision + deltaYVision* deltaYVision) -25
            
            #draw the distance label at each line end point 
            self.lineLabel = pyglet.text.Label( ( str(int(distance))+ " (" + str(int(self.X+deltaXVision)) + "," +str(int(self.Y+deltaYVision))+ ")"),
                font_name='Times New Roman',                      
                font_size=10,
                x=self.X+deltaXVision, y=self.Y+deltaYVision,
                anchor_x='center', anchor_y='center',color=(0, 0, 255, 255))
            self.lineLabel.draw()

        #display center of carBox Label info
        self.centerLabel = pyglet.text.Label(("Center X = " + str(int(self.X))+ " , Y = " + str(int(self.Y)) + ", Theta = " +  str(self.thetaRadian)),
                font_name='Times New Roman',                      
                font_size=15,
                x= 400, y=20,
                anchor_x='center', anchor_y='center',color=(0, 0, 255, 255))
        self.centerLabel.draw()

    def draw(self, x, y, thetaR):
        self.thetaRadian=thetaR
        self.X=x
        self.Y=y
        self.drawCarBox()
        self.drawVisionLine()
        






