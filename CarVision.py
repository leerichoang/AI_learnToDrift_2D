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

        
        self.lineLabel = pyglet.text.Label((str(int(self.carBoxX1[0])) + " , " + str(int(self.carBoxX1[1]))),
            font_name='Times New Roman',                      
            font_size=10,
            x=self.carBoxX1[0], y=self.carBoxX1[1],
            anchor_x='center', anchor_y='center',color=(0, (255), 0, 255))
        self.lineLabel.draw()
        
        self.lineLabel = pyglet.text.Label((str(int(self.carBoxY1[0])) + " , " + str(int(self.carBoxY1[1]))),
            font_name='Times New Roman',                      
            font_size=10,
            x=self.carBoxY1[0], y=self.carBoxY1[1],
            anchor_x='center', anchor_y='center',color=(0, (255), 0, 255))
        self.lineLabel.draw()

        self.lineLabel = pyglet.text.Label((str(int(self.carBoxX2[0])) + " , " + str(int(self.carBoxX2[1]))),
            font_name='Times New Roman',                      
            font_size=10,
            x=self.carBoxX2[0], y=self.carBoxX2[1],
            anchor_x='center', anchor_y='center',color=(0, (255), 0, 255))
        self.lineLabel.draw()

        self.lineLabel = pyglet.text.Label((str(int(self.carBoxY2[0])) + " , " + str(int(self.carBoxY2[1]))),
            font_name='Times New Roman',                      
            font_size=10,
            x=self.carBoxY2[0], y=self.carBoxY2[1],
            anchor_x='center', anchor_y='center',color=(0, (255), 0, 255))
        self.lineLabel.draw()


        

    def drawVisionLine(self):
        counter = 0
        color = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [0,255,255],
        [255,0,255], [128,128,0], [0,0,0]]
        colorNameKey = {-4:"RED", -3:"GREEN", -2:"BLUE", -1:"YELLOWR", 0:"TEAL", 1:"PURPLE", 2:"YELLOWL", 3:"BLACK"}

        #start manitude
        manitude=25
        for i in range(-4,4,1):
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
            
            #Check for horizontal line from outX1 to outX2
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
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
            
            #Check for horizontal line from outY1 to outY2
            if slope!=0:
                testxbounce = (660-b)/slope
            else:
                testxbounce = (660-b)
            if int(testxbounce) in range(40,1240):
                if self.isQuadrant1(updatedTheta):
                    if self.X>=40 and self.X <240:
                        if not(line240 or line260):
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=1040 and self.X < 1240:
                        testmanitude = (1240-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                            manitude = testmanitude
                        else:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=240 and self.X <1040:
                        if self.Y >=460 and self.Y <660:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                elif self.isQuadrant2(updatedTheta):
                    if self.X>=40 and self.X <240:
                        testmanitude = (40-self.X)/math.cos(updatedTheta)
                        deltaYVision = math.sin(updatedTheta) * testmanitude
                        if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                            manitude = testmanitude
                        else:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=1040 and self.X < 1240:
                        if not (line1040 or line260):
                            testmanitude = (40-self.X)/math.cos(updatedTheta)
                            deltaYVision = math.sin(updatedTheta) * testmanitude
                            if (self.Y + deltaYVision >= 60 and self.Y + deltaYVision < 660):
                                manitude = testmanitude
                            else:
                                manitude = ((testxbounce-self.X)/math.cos(updatedTheta))
                    elif self.X>=240 and self.X <1040:
                        if self.Y >=460 and self.Y <660:
                            manitude = ((testxbounce-self.X)/math.cos(updatedTheta))

            
            #manitude = min(manitude1,manitude2,manitude4)
            #calculate the x and y 
            deltaXVision = math.cos(updatedTheta) * manitude
            deltaYVision = math.sin(updatedTheta) * manitude
                
            #draw the line
            Line(self.X,self.Y,self.X+deltaXVision,self.Y+deltaYVision,color[counter],1).draw()
            
            #calculate the distance = c
            # a^2 + b^2 = c^2
            # c = sqrt(a^2 + b^2)
            # - 25 for from the center
            distance = math.sqrt(deltaXVision*deltaXVision + deltaYVision* deltaYVision) -25
            self.allDistance[colorNameKey[i]]=int(distance)

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
        #test out touching
        #   outY1(40,660) - - - - - - - -  outY2(1240,660)
        #    |  inY1(240,460) - - - - - inY2(1040,460) |
        #    |   |                                 |   |
        #    |   |                                 |   |
        #    |  inX1(240,260) - - - - - inX2(1040,260) | 
        #   outX1(40,60) - - - - - - - - -  outX2(1240,60)
        #1
        Line(240,260,240,60,[0,0,0],1).draw()
        #2
        Line(640,260,640,60,[0,0,0],1).draw()
        #3
        Line(1040,260,1040,60,[0,0,0],1).draw()
        #4
        Line(1040,260,1040,60,[0,0,0],1).draw()
        #5
        Line(1040,360,1240,360,[0,0,0],1).draw()
        #6
        Line(1040,460,1040,660,[0,0,0],1).draw()
        #7
        Line(640,460,640,660,[0,0,0],1).draw()
        #8
        Line(240,460,240,660,[0,0,0],1).draw()
        #9
        Line(240,360,40,360,[0,0,0],1).draw()
        #1End

        #Check Points
        if self.isCarBoxCollision([240,260],[240,60]):
            print("CheckPoint 1")
        elif self.isCarBoxCollision([640,260],[640,60]):
            print("CheckPoint 2")
        elif self.isCarBoxCollision([1040,260],[1040,60]):
            print("CheckPoint 3")
        elif self.isCarBoxCollision([1040,260],[1240,60]):
            print("CheckPoint 4")  
        elif self.isCarBoxCollision([1040,360],[1240,360]):
            print("CheckPoint 5")
        elif self.isCarBoxCollision([1040,460],[1040,660]):
            print("CheckPoint 6")
        elif self.isCarBoxCollision([640,460],[640,660]):
            print("CheckPoint 7")
        elif self.isCarBoxCollision([240,460],[240,660]):
            print("CheckPoint 8")  
        elif self.isCarBoxCollision([240,360],[40,360]):
            print("CheckPoint 9")  


    def isQuadrant1(self, rTheta):
        return (math.sin(rTheta) >=0 and math.cos(rTheta) >=0 and math.tan(rTheta) >=0)
    
    def isQuadrant2(self, rTheta):
        return (math.sin(rTheta) >=0 and math.cos(rTheta) <0 and math.tan(rTheta) <0)

    def isQuadrant3(self, rTheta):
        return (math.sin(rTheta) <0 and math.cos(rTheta) <0 and math.tan(rTheta) >=0)
    
    def isQuadrant4(self, rTheta):
        return (math.sin(rTheta) <0 and math.cos(rTheta) >=0 and math.tan(rTheta) <0)

    def isLineCollision(self, line1PointX1Y1, line1PointX2Y2, line2PointX1Y1, line2PointX2Y2):
        
        #y=mx+b
        #b=y - mx
        #x = (b-y)/m
        
        #Find equation of line1
        # line1PointX1Y1 = [x1,y1]
        # line1PointX2Y2 = [x2,y2]

        #slope    
        line1Rise = int(line1PointX2Y2[1] - line1PointX1Y1[1])
        line1Run = int(line1PointX2Y2[0] - line1PointX1Y1[0])
        line1Slope=0

        line1StartPoint = int(min(line1PointX1Y1[0], line1PointX2Y2[0]))
        line1EndPoint = int(max(line1PointX1Y1[0], line1PointX2Y2[0]))
        line1Ypoints ={}
        if line1Run!=0:
            line1Slope = line1Rise / line1Run
            line1B= int(line1PointX1Y1[1] - (line1Slope*line1PointX1Y1[0]))
            #line 1 equation
            #line1Function = y1
            # y1 = (line1Slope*x) + line1B
            for x in range(line1StartPoint, line1EndPoint+1):
                line1Ypoints[x] = int((line1Slope*x) + line1B)
            line1noSlope = False
        else:
            line1StartRange = int(min(line1PointX1Y1[1], line1PointX2Y2[1]))
            line1SEndRange = int(max(line1PointX1Y1[1], line1PointX2Y2[1]))
            for i in range(line1StartRange, line1SEndRange):
                line1Ypoints[i]=int(line1PointX1Y1[0])
            line1noSlope = True
        
        #Find equation of line2
        # line2PointX1Y1 = [x1,y1]
        # line2PointX2Y2 = [x2,y2]

        #slope    
        line2Rise = int(line2PointX2Y2[1] - line2PointX1Y1[1])
        line2Run = int(line2PointX2Y2[0] - line2PointX1Y1[0])
        line2Slope=0

        line2StartPoint = int(min(line2PointX1Y1[0], line2PointX2Y2[0]))
        line2EndPoint = int(max(line2PointX1Y1[0], line2PointX2Y2[0]))
        line2Ypoints ={}
        if line2Run!=0:
            line2Slope = line2Rise / line2Run
            line2B= int(line2PointX1Y1[1] - (line2Slope*line2PointX1Y1[0]))
            #line 2 equation
            #line2Function = y1
            # y2 = (line2Slope*x) + line2B
            for x in range(line2StartPoint, line2EndPoint+1):
                line2Ypoints[x] = int((line2Slope*x) + line2B)
            line2noSlope = False
        else:
            line2StartRange = int(min(line2PointX1Y1[1], line2PointX2Y2[1]))
            line2SEndRange = int(max(line2PointX1Y1[1], line2PointX2Y2[1]))
            for i in range(line2StartRange, line2SEndRange):
                line2Ypoints[i]=int(line2PointX1Y1[0])
            line2noSlope = True

        
        
        
        # #check for collision

        if line2noSlope and not line1noSlope:
            for x1, y1 in line1Ypoints.items():
                if y1 in line2Ypoints:
                    if x1==line2Ypoints[y1]:
                        return True
        elif line1noSlope and not line2noSlope:
            for x2, y2 in line2Ypoints.items():
                if y2 in line1Ypoints:
                    if x2==line1Ypoints[y2]:
                        return True
        elif not (line1noSlope or line2noSlope):
            for x1 in range(line1StartPoint, line1EndPoint+1):
                if line1Slope!=0:
                    expectedX1 = int(((line2Slope*x1) + line2B - line1B)/line1Slope)
                    if expectedX1 in range(line2StartPoint, line2EndPoint+1):
                        if expectedX1 in range(line1StartPoint, line1EndPoint+1):
                            return True
        elif (line1noSlope or line2noSlope):
            for y1, x1 in line1Ypoints.items():
                if y1 in line2Ypoints:
                    if line1Ypoints[y1] == line2Ypoints[y1]:
                        return True
        
    def isCarBoxLineX1X2Collision(self,line2PointX1Y1, line2PointX2Y2):
        return self.isLineCollision(self.carBoxX1,self.carBoxX2,line2PointX1Y1,line2PointX2Y2)
    def isCarBoxLineY1Y2Collision(self,line2PointX1Y1, line2PointX2Y2):
        return self.isLineCollision(self.carBoxY1,self.carBoxY2,line2PointX1Y1,line2PointX2Y2)
    def isCarBoxLineX1Y1Collision(self,line2PointX1Y1, line2PointX2Y2):
        return self.isLineCollision(self.carBoxX1,self.carBoxY1,line2PointX1Y1,line2PointX2Y2)
    def isCarBoxLineX2Y2Collision(self,line2PointX1Y1, line2PointX2Y2):
        return self.isLineCollision(self.carBoxX2,self.carBoxY2,line2PointX1Y1,line2PointX2Y2)
    def isCarBoxCollision(self,line2PointX1Y1, line2PointX2Y2):
        pam1 = line2PointX1Y1
        pam2 = line2PointX2Y2

        if (self.isCarBoxLineX1X2Collision(pam1, pam2) or self.isCarBoxLineY1Y2Collision(pam1, pam2) or self.isCarBoxLineX1Y1Collision(pam1, pam2) or self.isCarBoxLineX2Y2Collision(pam1, pam2)):
            return True
        else:
            return False
    
    #   outY1(40,660) - - - - - - - -  outY2(1240,660)
    #    |  inY1(240,460) - - - - - inY2(1040,460) |
    #    |   |                                 |   |
    #    |   |                                 |   |
    #    |  inX1(240,260) - - - - - inX2(1040,260) | 
    #   outX1(40,60) - - - - - - - - -  outX2(1240,60)
    def isInTrackCollision(self):
        return(self.isCarBoxCollision([240,260],[1040,260]) or self.isCarBoxCollision([240,460],[1040,460]) or self.isCarBoxCollision([240,260],[240,460]) or self.isCarBoxCollision([1040,260],[1040,460]))
    def isOutTrackCollision(self):
        return(self.isCarBoxCollision([40,60],[1240,60]) or self.isCarBoxCollision([40,660],[1240,660]) or self.isCarBoxCollision([40,60],[40,660]) or self.isCarBoxCollision([1240,60],[1240,660]))
    def isBothTrackCollision(self):
        if (self.isInTrackCollision()or self.isOutTrackCollision()):
            print("touch track")
            return True
        else:
            print("not")
            return False

    def getDistanceFromColorLine(self,color):
        return self.allDistance[color]
        



