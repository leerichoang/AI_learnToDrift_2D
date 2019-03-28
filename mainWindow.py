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
        self.clear()
        #self.glClear(GL_COLOR_BUFFER_BIT)
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


        glEnd()

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            print('turn left')
            self.car.updateTheta(-self.car.rotation_speed* dt)
        
        if self.key_handler[key.RIGHT]:
            print('turn right')
            self.car.updateTheta(self.car.rotation_speed* dt)
        
        if self.key_handler[key.UP]:
            thetaRadian = -math.radians(self.car.getTheta())
            deltaX = math.cos(thetaRadian) * self.car.speed * dt
            deltaY = math.sin(thetaRadian) * self.car.speed * dt
            self.car.updateX(deltaX)
            self.car.updateY(deltaY)
            self.car.updateDeltaX(deltaX)
            self.car.updateDeltaY(deltaY)
            print(str(self.car.getDeltaX())+' '+str(self.car.getDeltaY()))

        if self.key_handler[key.DOWN]:
            thetaRadian = -math.radians(self.car.getTheta())
            deltaX = math.cos(thetaRadian) * self.car.speed * dt
            deltaY = math.sin(thetaRadian) * self.car.speed * dt
            self.car.updateX(-deltaX)
            self.car.updateY(-deltaY)
            self.car.updateDeltaX(-deltaX)
            self.car.updateDeltaY(-deltaY)  

        self.car.updateX(self.car.getDeltaX())
        self.car.updateY(self.car.getDeltaY())
        self.car.updateDeltaX(self.car.getDeltaX() * 0.95)
        self.car.updateDeltaY(self.car.getDeltaY() * 0.95)

if __name__ == "__main__":
    window = MyWindow(WINDOWWIDTH,WINDOWHEIGHT, "DRIFT AI", resizable=True, vsync =True)
    window.push_handlers(window.key_handler)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()

@window.event 
def on_draw():
    # #glClear(GL_COLOR_BUFFER_BIT)
    # #glBegin(GL_LINES)
    # glVertex2i(25,75)
    # glVertex2i(55,66)

    # glVertex2i(80,100)
    # glVertex2i(70,500)
    glBegin(GL_LINES)
    # create a line, x,y,z
    glVertex3f(100.0,100.0,0.25)
    glVertex3f(200.0,300.0,-0.75)
    glEnd()
    print("here")