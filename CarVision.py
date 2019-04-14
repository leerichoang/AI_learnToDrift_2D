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
        self.allDistance = {}
    
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
        counter = 0
        color = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [0,255,255],
        [255,0,255], [128,128,0], [0,0,0]]



        manitude=25
        for i in range(0,4,4):
            rToAdd = i * math.pi/4 
            #rToAdd = 0 * math.pi/4 
            updatedTheta=self.thetaRadian + rToAdd
            
            #y=mx+b
            #b=y - mx
            #x = (b-y)/m
            
            #find slope
            slope=math.tan(updatedTheta)

            #find y intercept b=y - mx
            b = self.Y - slope*self.X
            
            #   outY1(40,660) - - - - - - - -  outY2(1240,660)
            #    |  inY1(240,460) - - - - - inY2(1040,460) |
            #    |   |                                 |   |
            #    |   |                                 |   |
            #    |  inX1(240,260) - - - - - inX2(1040,260) | 
            #   outX1(40,60) - - - - - - - - -  outX2(1240,60)
            
            line40 = False
            line240 = False
            line1040 = False
            line1240 = False
            #Check for All Verical line Interception
            #broke up into location of car in height (self.Y)
            #   then quadrant and location of car in width(self.X)
            if (self.Y < 260 and self.Y >=60):
                #quad 1 
                if self.isQuadrant1(updatedTheta):
                    if (self.X < 240 and self.X >=40):
                        testmanitude = (240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision > 260 and self.Y + deltaYVision <= 460):
                            manitude = testmanitude
                            line240 = True  
                        else:
                            manitude = (1240-self.X)/math.cos(updatedTheta)
                            line1240 = True
                    else:
                        manitude = (1240-self.X)/math.cos(updatedTheta)
                        line1240 = True
                #quad 4
                elif self.isQuadrant4(updatedTheta):
                    manitude = (1240-self.X)/math.cos(updatedTheta)
                    line1240 = True
                #quad 2
                elif self.isQuadrant2(updatedTheta):
                    if (self.X < 240 and self.X >=40):
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True
                    elif (self.X >=1040 and self.X <1240):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision > 260 and self.Y + deltaYVision <= 460):
                            manitude = testmanitude
                            line1040 = True  
                        else:
                            manitude = (40-self.X)/math.cos(updatedTheta)
                            line40 = True
                    else:
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True

                #quad 3
                elif self.isQuadrant3(updatedTheta):
                    if (self.X < 240 and self.X >=40):
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True
                    elif (self.X >=1040 and self.X <1240):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision > 260 and self.Y + deltaYVision <= 460):
                            manitude = testmanitude
                            line1040 = True  
                        else:
                            manitude = (40-self.X)/math.cos(updatedTheta)
                            line40 = True
                    else:
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True

            elif (self.Y>=260 and self.Y <460):
                if self.X <= 240 and self.X >=40:
                    #quad1
                    if self.isQuadrant1(updatedTheta):
                        testmanitude = (240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line240 = True   
                    #quad 4
                    elif self.isQuadrant4(updatedTheta):
                        testmanitude = (240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line240 = True
                    #quad 2
                    elif self.isQuadrant2(updatedTheta):
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True
                    #quad 3
                    elif self.isQuadrant3(updatedTheta):
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True
                elif self.X >=1040 and self.X <1240:
                    #quad1
                    if self.isQuadrant1(updatedTheta):
                        manitude = (1240-self.X)/math.cos(updatedTheta)
                        line1240 = True
                    #quad 4
                    elif self.isQuadrant4(updatedTheta):
                        manitude = (1240-self.X)/math.cos(updatedTheta)
                        line1240 = True
                    #quad 2
                    elif self.isQuadrant2(updatedTheta):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line1040 = True
                    #quad 3
                    elif self.isQuadrant3(updatedTheta):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line1040 = True

                    
            elif (self.Y >= 460 and self.Y < 660):
                #quad 1 
                if self.isQuadrant1(updatedTheta):
                    if (self.X < 240 and self.X >=40):
                        testmanitude = (240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision > 260 and self.Y + deltaYVision <= 460):
                            manitude = testmanitude
                            line240 = True  
                        else:
                            manitude = (1240-self.X)/math.cos(updatedTheta)
                            line1240 = True
                    else:
                        manitude = (1240-self.X)/math.cos(updatedTheta)
                        line1240 = True
                #quad 4
                elif self.isQuadrant4(updatedTheta):
                    if (self.X < 240 and self.X >=40):
                        testmanitude = (240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision > 260 and self.Y + deltaYVision <= 460):
                            manitude = testmanitude
                            line240 = True  
                        else:
                            manitude = (1240-self.X)/math.cos(updatedTheta)
                            line1240 = True
                    else:
                        manitude = (1240-self.X)/math.cos(updatedTheta)
                        line1240 = True
                #quad 2
                elif self.isQuadrant2(updatedTheta):
                    if (self.X >= 1040 and self.X <1240):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line1040 = True
                        else:
                            manitude = (40-self.X)/math.cos(updatedTheta)
                            line40 = True
                    else:
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True
                #quad 3
                elif self.isQuadrant3(updatedTheta):
                    if (self.X >= 1040 and self.X <1240):
                        testmanitude = (1040-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 260 and self.Y + deltaYVision < 460):
                            manitude = testmanitude
                            line1040 = True
                        else:
                            manitude = (40-self.X)/math.cos(updatedTheta)
                            line40 = True
                    else:
                        manitude = (40-self.X)/math.cos(updatedTheta)
                        line40 = True

            line260=False
            line460=False
            #Check for all horizontal lines
            #Check for horizontal line from inX1 to inX2
            if slope!=0:
                testxbounce = (260-b)/slope
            else:
                testxbounce = (260-b)        
            if int(testxbounce) in range(240,1040):
                if self.isQuadrant1(updatedTheta):
                    if self.Y < 260:
                        manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                        line260=True 
                elif self.isQuadrant2(updatedTheta):
                    if self.Y < 260:
                        manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                        line260=True 
            
            #Check for horizontal line from inY1 to inY2
            if slope!=0:
                    testxbounce = (460-b)/slope
            else:
                testxbounce = (460-b)        
            if int(testxbounce) in range(240,1040):
                if self.isQuadrant3(updatedTheta):
                    if self.Y >= 460:
                        manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                        line460=True  
                elif self.isQuadrant4(updatedTheta):
                    if self.Y >= 460:
                        manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                        line460=True 
            
            if slope!=0:
                testxbounce = (60-b)/slope
            else:
                testxbounce = (60-b)
            if int(testxbounce) in range(40,1240):
                if self.isQuadrant4(updatedTheta):
                    if self.X>=40 and self.X <240:
                        if not(line240 or line460):
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=1040 and self.X < 1240:
                        testmanitude = (1240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                            manitude = testmanitude
                        else:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=240 and self.X <1040:
                        if self.Y >=60 and self.Y <260:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                elif self.isQuadrant3(updatedTheta):
                    if self.X>=40 and self.X <240:
                        if not (line1040 or line460):
                            testmanitude = (40-self.X)/math.cos(updatedTheta)
                            deltaYVision = math.sin(updatedTheta) * testmanitude
                            if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                                manitude = testmanitude
                            else:
                                manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=1040 and self.X < 1240:
                        if not (line1040 or line460):
                            testmanitude = (40-self.X)/math.cos(updatedTheta)
                            deltaYVision = math.sin(updatedTheta) * testmanitude
                            if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                                manitude = testmanitude
                            else:
                                manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=240 and self.X <1040:
                        if self.Y >=60 and self.Y <260:
                            testmanitude = (40-self.X)/math.cos(updatedTheta)
                            deltaYVision = math.sin(updatedTheta) * testmanitude
                            if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                                manitude = testmanitude
                            else:
                                manitude = ((testxbounce-self.X)/math.cos(updatedTheta))

            


        

                    







            #manitude = min(manitude1,manitude2,manitude4)
            #calculate the x and y 
            deltaXVision = math.cos(self.thetaRadian+ rToAdd) * manitude
            deltaYVision = math.sin(self.thetaRadian+ rToAdd) * manitude
                
            #draw the line
            Line(self.X,self.Y,self.X+deltaXVision,self.Y+deltaYVision,color[counter],1).draw()
            
            #calculate the distance = c
            # a^2 + b^2 = c^2
            # c = sqrt(a^2 + b^2)
            # - 25 for from the center
            distance = math.sqrt(deltaXVision*deltaXVision + deltaYVision* deltaYVision) -25
            self.allDistance[i]=int(distance)

            #draw the distance label at each line end point 
            self.lineLabel = pyglet.text.Label( ( str(int(distance))+ " (" + str(int(self.X+deltaXVision)) + "," +str(int(self.Y+deltaYVision))+ ")"),
                font_name='Times New Roman',                      
                font_size=10,
                x=self.X+deltaXVision, y=self.Y+deltaYVision,
                anchor_x='center', anchor_y='center',color=(0, (50 * i%250), (30 * i%250), 255))
            self.lineLabel.draw()
            counter+=1

        #display center of carBox Label info
        self.centerLabel = pyglet.text.Label(("Center X = " + str(int(self.X))+ " , Y = " + str(int(self.Y)) + ", Theta = " +  str(self.thetaRadian/math.pi)+ " pi Degree = " + str(math.degrees(self.thetaRadian))),
                font_name='Times New Roman',                      
                font_size=15,
                x= 400, y=20,
                color=(0, 0, 255, 255))
        self.centerLabel.draw()

        self.centerLabel = pyglet.text.Label(("All Distance: "+ str(self.allDistance)),
            font_name='Times New Roman',                      
            font_size=15,
                x=40 , y=700,color=(0, 0, 255 , 255))
        self.centerLabel.draw()
        
        

    def draw(self, x, y, thetaR):
        self.thetaRadian=thetaR
        self.X=x
        self.Y=y
        self.drawCarBox()
        self.drawVisionLine()
        
    def isQuadrant1(self, rTheta):
        return (math.sin(rTheta) >=0 and math.cos(rTheta) >=0 and math.tan(rTheta) >=0)
    
    def isQuadrant2(self, rTheta):
        return (math.sin(rTheta) >=0 and math.cos(rTheta) <0 and math.tan(rTheta) <0)

    def isQuadrant3(self, rTheta):
        return (math.sin(rTheta) <0 and math.cos(rTheta) <0 and math.tan(rTheta) >=0)
    
    def isQuadrant4(self, rTheta):
        return (math.sin(rTheta) <0 and math.cos(rTheta) >=0 and math.tan(rTheta) <0)

