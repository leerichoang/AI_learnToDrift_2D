from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
import math 
WINDOWWIDTH=1280
WINDOWHEIGHT=720 

class CarSprite():
    def __init__(self):
        self.carSprite_image = pyglet.image.load('car_sprite_resized10percent.png')
        self.carSprite= pyglet.sprite.Sprite(self.carSprite_image, WINDOWWIDTH/2,WINDOWHEIGHT/2)
        self.x = self.carSprite.x
        self.y = self.carSprite.y
        self.theta = self.carSprite.rotation
        self.speed = 200.0
        self.rotation_speed = 200.0
        self.deltaX = 0.0
        self.deltaY = 0.0
        print(self.carSprite.width)
        print(self.carSprite.height)
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
    

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        glClearColor(1,1.0,1.0,1)
        self.fps_display = FPSDisplay(self)
        self.car = CarSprite()
        print(self.car.theta)
        self.key_handler = key.KeyStateHandler()


    def on_draw(self):
        self.clear()
        self.car.draw()
        self.fps_display.draw()


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
            self.car.updateX(deltaX*1.1)
            self.car.updateY(deltaY*1.1)
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