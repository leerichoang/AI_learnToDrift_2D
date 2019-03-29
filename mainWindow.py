from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math
from CarSprite import *
WINDOWWIDTH=1280
WINDOWHEIGHT=720 
class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        #this clear thing affect the background color
        #comment it out to get a black background
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.car = CarSprite()
        print(self.car.theta)
        self.key_handler = key.KeyStateHandler()


    def on_draw(self):
        #self.clear()
        glClear(GL_COLOR_BUFFER_BIT)
        self.car.draw()
        self.fps_display.draw()
        
        #outer Box
        glBegin(GL_LINES)
        #this color thing affect the lines
        glColor3f(1,0,0)
        # create a line, x,y,z
        glVertex3f(40.0,20.0,1)
        glVertex3f(40.0,700,1)

        glVertex3f(1240.0,20.0,1)
        glVertex3f(1240.0,700.0,1)
        
        glVertex3f(40.0,20.0,1)
        glVertex3f(1240.0,20.0,1)

        glVertex3f(40.0,700.0,1)
        glVertex3f(1240.0,700.0,1)

        #inner Box
        # create a line, x,y,z
        glVertex3f(240.0,220.0,1)
        glVertex3f(240.0,500.0,1)

        glVertex3f(1040.0,220.0,1)
        glVertex3f(1040.0,500.0,1)
        
        glVertex3f(240.0,220.0,1)
        glVertex3f(1040.0,220.0,1)

        glVertex3f(240.0,500.0,1)
        glVertex3f(1040.0,500.0,1)

        thetaRadian = -math.radians(self.car.getTheta())
        deltaX = math.cos(thetaRadian) * self.car.speed 
        deltaY = math.sin(thetaRadian) * self.car.speed 

        glVertex3f(self.car.getX(),self.car.getY()+(self.car.height/2),1)
        glVertex3f(self.car.getX()+deltaX,self.car.getY()+deltaY+(self.car.height/2),1)
        #print("here"+str(self.car.getTheta()))
        glEnd()

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            print('turn left')
            self.car.turnLeft(dt)
        
        if self.key_handler[key.RIGHT]:
            print('turn right')
            self.car.turnRight(dt)

        if self.key_handler[key.UP]:
            self.car.goStraight(dt)
            print(str(self.car.getDeltaX())+' '+str(self.car.getDeltaY()))

        if self.key_handler[key.DOWN]:
            self.car.goReverse(dt)
        self.car.runningCar(dt)

if __name__ == "__main__":
    window = MyWindow(WINDOWWIDTH,WINDOWHEIGHT, "DRIFT AI", resizable=True, vsync =True)
    window.push_handlers(window.key_handler)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()